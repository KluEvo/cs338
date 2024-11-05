from mistralai import Mistral
import re
from api_key import getApiKey
import requests
import json
import os
import time

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
    prompt = f"Identify and give a very simplified generic story structure in bullets that results ends with '{ending_state}', given the context that '{starting_state}'. Format the output with headings describing the plot structure and for each heading, give a vague description."
    return call_llm_api(prompt)

def generate_story_beats(sentence, context):
    if sentence.strip():
        print("waiting")
        time.sleep(2)
        prompt = f"Generate a short, casually written 1 sentence example scenario of the following part of the plot structure: '{sentence}', given the context of {context}"
        beat = call_llm_api(prompt)
        
        return beat

def export_beats_to_files(beats, output_dir="story_beats"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, beat in enumerate(beats, start=1):
        file_path = os.path.join(output_dir, f"beat_{i}.txt")
        with open(file_path, "w") as file:
            file.write(beat)
        print(f"Beat {i} exported to {file_path}")


def main():
    starting_state, ending_state = get_user_input()
    story_structure = identify_story_structure(starting_state, ending_state)
    print("Identified Story Structure:")
    # print(story_structure)
    beats = []
    options = []
    for part in story_structure.split('\n'):
        if part.strip():
            part = part.strip()
            # if part[0].lower() == 'a' or part[0].lower() == '1':
            #     print("How do you want this to play out?")

            #     options.append(part)
            
            print(part)
            # if part[0].lower() == 'b' or part[0].lower() == '2':
            
            #     choice = input()
            #     if choice.lower() == 'a' or choice.lower() == '1':
            #         beats.append(options[0])
            #     elif choice.lower() == 'b' or choice.lower() == '2':
            #         beats.append(options[1])
            #     else:
            #         print("not valid choice, defaulting to option A")
            #     options = []
    print(beats)



    # story_beats = generate_story_beats(story_structure)
    # export_beats_to_files(story_beats)

if __name__ == "__main__":
    # main()
    print(generate_story_beats("Amy and John’s rivalry becomes public when they have a spat during an important event or meeting, causing their boss or friends to impose “team-building” exercises on them", "John and Amy start to see each other’s strengths—John realizes Amy’s meticulous attention to detail, and Amy notices John’s creativity"))
