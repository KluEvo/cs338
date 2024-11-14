from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from storyBeats import get_user_input, identify_story_structure, generate_story_choices, find_options
# from namerecognition import extract_names
import random
import time

starting_state = ""
ending_state = ""
beats = []
context = ""
heldInfo = ""
heldInfoOld = ""
opts = ""


app = Flask(__name__)
cors = CORS(app) 
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/entry', methods=['GET', 'POST'])
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

    # starting_state = "Jon and Amy are rivals"
    # ending_state = "Jon and Amy start dating"
    story_structure = identify_story_structure(starting_state, ending_state)
    # print("Identified Story Structure:")
    # print(story_structure)
    return [story_structure.split('\n')]

@app.route('/characters2', methods=['GET', 'POST'])
def handelText(txt):
    global context
    global heldInfo
    global opts

    output = ""
    giveChoice = False
    if part.strip():
        part = part.strip()    
        if part[0].lower() == '*' or part[0].lower() == '-' :
            context += part + " "
            output = part
        elif context != "":
            opts = generate_story_choices(context, heldInfo, ending_state)
            output = opts
            heldInfo = part
            giveChoice = True

    return {
        "outputTxt": output,
        "choices": giveChoice
    }

def handleChoices(choice):
    global ending_state
    global beats
    global heldInfoOld
    global opts

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
    context = ""
    beats.append(choice)
    return choice

if __name__ == '__main__':
    app.run(debug=True) 