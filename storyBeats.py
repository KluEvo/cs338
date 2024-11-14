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
    prompt = f"Identify and give a very simplified generic story structure in bullets that results ends with '{ending_state}', given the context that '{starting_state}'. Format the output with headings (example: I. Introduction) describing the plot structure and for each heading, give a vague description."
    return call_llm_api(prompt)

def generate_story_choices(context, pstruct, ending_state):
    if context.strip():
        # print("waiting")
        time.sleep(1)
        prompt = f"in a story that seeks to end up with {ending_state} and given the context of {context}, give me between one and two possible outcome options, 1~2 sentences each, at the stage of only the {pstruct}. the options should be labeled (pre-pended with just) A. and B. Give only the options."
        beat = call_llm_api(prompt)
        
        time.sleep(1)
        return beat

def generate_story_beats(sentence, context):
    if sentence.strip():
        # print("waiting")
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
tesssws = """A. During a joint project or competition, a unexpected event forces Jon and Amy to work closely together. Their mutual respect and shared experiences lead to a deeper understanding of each other's strengths and weaknesses, eventually leading to a romantic connection.

B. A personal setback or challenge pushes both Jon and Amy to seek help from each other. As they share their struggles and support each other, their rivalry fades and they realize they have feelings for each other, ultimately leading to a romantic relationship."""

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
    # starting_state, ending_state = get_user_input()
    starting_state = "Jon and Amy are rivals"
    ending_state = "Jon and Amy start dating"
    story_structure = identify_story_structure(starting_state, ending_state)
    print("Identified Story Structure:")
    # print(story_structure)
    beats = []
    context = ""
    for part in story_structure.split('\n'):
        if part.strip():
            part = part.strip()
            # roman_pattern = re.compile(r'IX|IV|V?I{0,3}\.')

            # Check if the text matches the pattern
            
            if part[0].lower() == '*' or part[0].lower() == '-' :
            #     print("How do you want this to play out?")
                context += part + " "
            # if bool(roman_pattern.match(part)):
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

    # write a function that detects whether it is heading, context, or outcome.


if __name__ == "__main__":
    main()
    # print(generate_story_beats("John overhears Amy saying something surprisingly complimentary about him, which he misinterprets as sarcasm, leading to a funny, escalating misunderstanding that ends with both of them laughing (or maybe shouting) and admitting there’s something more between them", "John overhears Amy saying something surprisingly complimentary about him, which he misinterprets as sarcasm, leading to a funny, escalating misunderstanding that ends with both of them laughing (or maybe shouting) and admitting there’s something more between them"))
    # a = "VII. Setup"
    # roman_pattern = re.compile(r'IX|IV|V?I{0,3}\.')
    # print(roman_pattern.match(a))
