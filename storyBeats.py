from mistralai import Mistral
import re
from api_key import getApiKey
import requests
import json
import os
import time
import re

api_key = getApiKey()

model = "open-mistral-7b"
client = Mistral(api_key=api_key)

def getMistralInfo():
    return model, client

def call_llm_api(prompt):
    model, client = getMistralInfo()
    chat_response = client.chat.complete(
        model=model,
        messages=[{"role":"user", "content":f"{prompt}?"}]
    )
    info = chat_response.choices[0].message.content
    return info


def get_user_input():
    starting_state = input("Enter the starting state of the character: ")
    ending_state = input("Enter the ending state of the character: ")
    return starting_state, ending_state

def identify_story_structure(starting_state, ending_state):
    prompt = f"Identify and give a very simplified generic five part story structure in bullets that results ends with '{ending_state}', given the context that '{starting_state}'. Start with inciding incident and end with resolution. Format the output with headings (example: I. Inciding Incident) describing the plot structure. each description should be labeled (pre-pended with just) '-' "
    return call_llm_api(prompt)

def generate_story_choices(context, pstruct, ending_state):
    if context.strip():
        time.sleep(1)
        prompt = f"in a story that seeks to end up with {ending_state} and given the context of {context}, give me between two possible outcome options, 1~2 short sentences each. the options should develop the plot in different ways and should make sense with the both this context and given that this just for the {pstruct} story structure, do not resolve any conflicts before we reach the conclusion/resolution story structure. The options should be labeled (and only pre-pended with) A. and B., respectively. Give only the options."
        beat = call_llm_api(prompt)
        time.sleep(1)
        return beat

def generate_story_beats(sentence, context):
    if sentence.strip():
        time.sleep(1)
        prompt = f"Generate a very brief, casually written 1 sentence example scenario of the following part of the plot structure: '{sentence}', given the context of {context}"
        beat = call_llm_api(prompt)
        
        time.sleep(1)
        return beat

def export_beats_to_files(beats, output_dir="story_beats"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, beat in enumerate(beats, start=1):
        file_path = os.path.join(output_dir, f"beat_{i}.txt")
        with open(file_path, "w") as file:
            file.write(beat)
        print(f"Beat {i} exported to {file_path}")

def find_options(text):
    options = []
    for line in text.split('\n'):
        if not line:
            continue
        elif line[0].lower() == 'a':
            options.append(line[2:].strip())
        elif line[0].lower() == 'b':
            options.append(line[2:].strip())
    return options 


def main():
    starting_state = "Jon and Amy are rivals"
    ending_state = "Jon and Amy start dating"
    story_structure = identify_story_structure(starting_state, ending_state)
    print("Identified Story Structure:")
    beats = []
    context = ""
    for part in story_structure.split('\n'):
        if part.strip(): 
            part = part.strip()
            
            if part[0].lower() == '*' or part[0].lower() == '-' :
                context += part + " "
            elif context != "":
                print("aaa")
                opts = generate_story_choices(context, part, ending_state)
                print(opts)
                options = find_options(opts)
                choice = input("How do you want this to play out? ")
                if choice.lower() == 'a' or choice.lower() == '1':
                    choice = options[0]
                elif choice.lower() == 'b' or choice.lower() == '2':
                    choice = options[1]
                else:
                    print("not valid choice, defaulting to the first option.")
                    choice = options[0]
                beat = generate_story_beats(choice, context)
                print(beat)
                beats.append(beat)

                context = ""
            print(part)
            
    print(beats)




if __name__ == "__main__":
    main()