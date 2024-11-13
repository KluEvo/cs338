import re

def identify_story_component(line):
    # Pattern definitions
    heading_pattern = re.compile(r"\b[IVXLCDM]+\b")  # Checks for Roman numeral anywhere in the line
    context_pattern = re.compile(r"\*")  # Checks for * anywhere in the line
    outcome_pattern = re.compile(r"^(A|B|1|2)\.")  # Checks if line starts with a., b., 1., or 2.
    
    # Check and return the type based on the pattern match
    if heading_pattern.search(line):
        return "Heading"
    elif context_pattern.search(line):
        return "Context"
    elif outcome_pattern.match(line):
        return "Outcome"
    else:
        return "Unknown"

# Example usage
lines = [
    "A: Amy and John’s rivalry becomes public when they have a spat during an important event or meeting, causing their boss or friends to impose “team-building” exercises on them."
    "B: Their friends, tired of the tension, decide to “help” by setting them up in situations that force them to see the other’s positive side (e.g., team dinners, happy hours, and casual “double dates”)."
]

for line in lines:
    print(f"'{line}' is a(n): {identify_story_component(line)}")
