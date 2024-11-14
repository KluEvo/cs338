from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from storyBeats import get_user_input, identify_story_structure, generate_story_choices, find_options, generate_story_beats
# from namerecognition import extract_names
import random
import time

starting_state = ""
ending_state = ""
beats = []
context = ""
heldInfo = ""
opts = ""


app = Flask(__name__)
cors = CORS(app) 
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/entry', methods=['POST'])
def getUserPrompt():
    global starting_state
    global ending_state
    global beats
    global context
    beats = []
    context = ""
    data = request.get_json()
    starting_state = data['starting_state']
    ending_state = data['ending_state']
    story_structure = identify_story_structure(starting_state, ending_state)
    return jsonify({'story_structure': story_structure.split('\n')})

@app.route('/text', methods=['POST'])
def handleText():
    global context
    global heldInfo
    global opts
    # print(context)
    data = request.get_json()
    part = data["txt"]
    output = ""
    giveChoice = False
    if part.strip():
        part = part.strip()    
        if part[0].lower() == '*' or part[0].lower() == '-' :
            context += part + " "
            output = part
        elif context != "":
            print("HERE")
            opts = generate_story_choices(context, heldInfo, ending_state)
            output = opts
            heldInfo = part
            giveChoice = True

    return {
        "outputTxt": output,
        "choices": giveChoice
    }

@app.route('/choices', methods=['POST'])
def handleChoices():
    global ending_state
    global beats
    global heldInfo
    global opts


    data = request.get_json()
    choice = data['choice']
    print(choice)

    # print(opts)
    options = find_options(opts)
    # choice = input("How do you want this to play out? ")
    if choice.lower() == 'a':
        choice = options[0]
    elif choice.lower() == 'b':
        choice = options[1]
    else:
        print("not valid choice, defaulting to the first option.")
        choice = options[0]
    
    beat = generate_story_beats(choice, context)
    beats.append(beat)

    context = ""
    return jsonify({
        "choice":choice,
        "otherprint": heldInfo
    })





@app.route('/start', methods=['POST'])
def start():
    data = request.json
    starting_state = data.get('starting_state')
    ending_state = data.get('ending_state')
    story_structure = identify_story_structure(starting_state, ending_state)
    return jsonify({'story_structure': story_structure.split('\n')})

@app.route('/generate_choices', methods=['POST'])
def generate_choices():
    data = request.json
    context = data.get('context')
    part = data.get('part')
    ending_state = data.get('ending_state')
    opts = generate_story_choices(context, part, ending_state)
    options = find_options(opts)
    return jsonify({'options': options})

@app.route('/generate_beats', methods=['POST'])
def generate_beats():
    data = request.json
    choice = data.get('choice')
    context = data.get('context')
    beat = generate_story_beats(choice, context)
    return jsonify({'beat': beat})

if __name__ == '__main__':
    port_number = 5001
    app.run(debug=True, host='localhost', port=port_number)