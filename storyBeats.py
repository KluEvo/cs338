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
    prompt = f"Identify and give a very simplified generic story structure (in bullets, with options) that results ends with '{ending_state}', given the context that '{starting_state}'. "
    return call_llm_api(prompt)

def generate_story_beats(story_structure):
    beats = []
    for part in story_structure.split('\n'):
        if part.strip():
            print("waiting")
            time.sleep(5)
            prompt = f"Generate a story beat for the following part of the plot structure: '{part}'."
            beat = call_llm_api(prompt)
            beats.append(beat)
    return beats

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
    for part in story_structure.split('\n'):
        if part.strip():
            print(part)

    # story_beats = generate_story_beats(story_structure)
    # export_beats_to_files(story_beats)

    # write a function that detects whether it is heading, context, or outcome.


if __name__ == "__main__":
    main()
