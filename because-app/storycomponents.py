import re

def identify_story_component(line):
    # Pattern definitions
    heading_pattern = re.compile(r"\b[IVXLCDM]+\b")  # Checks for Roman numeral anywhere in the line
    context_pattern = re.compile(r"\*")  # Checks for * anywhere in the line
    outcome_pattern = re.compile(r"^(a|b|1|2)\.")  # Checks if line starts with a., b., 1., or 2.
    
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
    "I. Introduction",
    "* A common obstacle arises that requires collaboration between Jane and Amy.",
    "a. Jane and Amy are on the verge of losing their scholarships.",
    "1. Jane and Amy are on the verge of losing their scholarships",
    "Some unrelated sentence without markers."
]

for line in lines:
    print(f"'{line}' is a(n): {identify_story_component(line)}")
