import spacy
from fuzzywuzzy import fuzz
import re

# Load the English language model
nlp = spacy.load("en_core_web_sm")


def match_format(text, known_person, known_award):
    # Regular expression to extract parts before and after "wins"
    pattern = r"(.+?)\s+wins\s+(.+)"
    matchRes = re.match(pattern, text)

    if not matchRes:
        return False

    # Extract the parts before and after "wins"
    person_part = matchRes.group(1)
    award_part = matchRes.group(2)

    # Define a function to check if a part matches the known person or award
    def matches_name(part, known):
        return fuzz.ratio(part.lower(), known.lower()) > 50
    
    def matches_award(part, known):
        # Tokenize the known award and the part to compare tokens
        known_tokens = nlp(known.lower())
        part_tokens = nlp(part.lower())

        # Additional check for the presence of the word "best"
        if "best" not in part.lower():
            return False

        
        known_tokens_list = [token.text for token in known_tokens]
        part_tokens_list = [token.text for token in part_tokens]

        known_index = known_tokens_list.index("best") + 1
        part_index = part_tokens_list.index("best") + 1

        print(known_tokens_list[known_index])
        print(part_tokens_list[part_index])

        if known_index < len(known_tokens_list) and part_index < len(part_tokens_list):
            if fuzz.ratio(known_tokens_list[known_index], part_tokens_list[part_index]) > 80:
                return True

        return False
        # return 



    # Check if the extracted parts match the known person and award
    if matches_name(person_part, known_person) and matches_award(award_part, known_award):
        return True

    return False


# Example usage
baseNO = "JDoe wins Best Actor"
known_person = "John Doe"
known_award = "Best Actor in a Motion Picture – Drama"

print(match_format(baseNO, known_person, known_award))
