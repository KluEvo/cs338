from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from storyBeats import get_user_input, identify_story_structure, generate_story_choices, find_options, generate_story_beats
# from namerecognition import extract_names
import random
import time

starting_state = ""
ending_state = ""
beats = []
storyStruct = ""
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
    global storyStruct
    global context
    beats = []
    context = ""
    data = request.get_json()
    starting_state = data['starting_state']
    ending_state = data['ending_state']
    story_structure = identify_story_structure(starting_state, ending_state)
    print("Flask python code Story Structure: ", story_structure)
    storyStruct = story_structure
    return jsonify({'story_structure': story_structure.split('\n')})

@app.route('/text', methods=['POST'])
def handleText():
    global context
    global heldInfo
    global opts
    
    giveChoice = False
    # print(context)
    data = request.get_json()
    lines = data["txt"]
    output = []

    
    # print("this is lines: ", lines)
    for line in lines:
        if line.strip():
            part = line.strip()    
            print("this is part: ", part)
            if part[0].lower() == '*' or part[0].lower() == '-' :
                part = part[1:]
                context += part + " "
            else:    
                heldInfo = part
            output.append(part)
 
    print("heldInfo:", heldInfo)
    opts = generate_story_choices(context, heldInfo, ending_state)
    ch = []
    opts = opts.split('\n')
    print("this is opts: ", opts)
    for line in opts:
        if line.strip():
            part = line.strip()    
            ch.append(part)
    # print("this is the pstruct after: ", heldInfo)
    # print(ch)
    opts = ch
    return jsonify({
        "outputTxt": output,
        "choices": opts
    })


@app.route('/choices', methods=['POST'])
def handleChoices():
    global ending_state
    global beats
    global heldInfo
    global opts
    global context


    data = request.get_json()
    choice = data['choice']

    # print(opts)
    options = opts
    print(options)
    # choice = input("How do you want this to play out? ")
    if choice.lower() == 'a':
        choice = options[0]
    elif choice.lower() == 'b':
        choice = options[1]
    else:
        print("not valid choice, defaulting to the first option.")
        choice = options[0]
    choice = choice[1:]
    print(choice)
    print("heldInfo Choices:", heldInfo)
    beat = generate_story_beats(choice, context)
    if beat:
        beat = beat.strip('"')
    beats.append(beat + " ")

    context = ""
    return jsonify({
        "result":beat,
        "otherprint": heldInfo
    })



if __name__ == '__main__':
    port_number = 5001
    app.run(debug=True, host='localhost', port=port_number)