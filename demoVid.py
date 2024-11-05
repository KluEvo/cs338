import re
from storyBeats import generate_story_beats

def identify_story_component(line):
    # Pattern definitions
    heading_pattern = re.compile(r"\b[IVXLCDM]+\b")  # Checks for Roman numeral anywhere in the line
    context_pattern = re.compile(r"\*")  # Checks for * anywhere in the line
    outcome_pattern = re.compile(r"^(A|B|1|2)\:")  # Checks if line starts with a., b., 1., or 2.
    
    # Check and return the type based on the pattern match
    if heading_pattern.search(line):
        return "Heading"
    elif context_pattern.search(line):
        return "Context"
    elif outcome_pattern.match(line):
        return "Outcome"
    else:
        return "Unknown"



def load_file_to_list(file_path):
    try:
        with open(file_path, 'r', encoding="utf8") as file:
            lines = file.readlines()
            # Remove newline characters from each line
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
file_path = 'example.txt'  # Replace with your file path
lines = load_file_to_list(file_path)
def getType(line):
    return identify_story_component(line)

beats = []
options = []
context = ""
input("Enter the starting state of the character:")
input("Enter the ending state of the character:")
for line in lines:
    if getType(line) == "Heading":
        input()
        print(line)
                
    elif getType(line) == "Context":
        print(line)
        context += line
        continue
    elif getType(line) == "Outcome":
        if line[0].lower() == 'a' or line[0].lower() == '1':
            print("How do you want this to play out?")
            print(line)
            options.append(line)
        elif line[0].lower() == 'b' or line[0].lower() == '2':
            print(line)        
            choice = input()
            if choice.lower() == 'a' or choice.lower() == '1':
                choice = options[0]
            elif choice.lower() == 'b' or choice.lower() == '2':
                choice = options[1]
            else:
                print("not valid choice, defaulting to the first option.")
            beat = generate_story_beats(choice, context)
            print(beat)
            beats.append(beat)
            options = []
            context = ""
    else:
        if not options:
            beat = generate_story_beats(context, context)
            beats.append(beat)

print(beats)