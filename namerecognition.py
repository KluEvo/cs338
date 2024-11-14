import spacy
import requests
from bs4 import BeautifulSoup
from google_search_api.google_search_api import GoogleSearchAPI

# pip install google-opensearch-api
# pip install spacy
# pip install bs4

# python3 -m spacy download en_core_web_lg


# Load the English language model



def extract_names(sentence):
    # Process the sentence using the language model
    doc = nlp(sentence)

    names_dict = {}
    person_count = 1

    # Extract names (proper nouns) from the sentence
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names_dict[f"person {person_count}"] = ent.text
            person_count+=1
    return names_dict

# Example usage
sentence = input("Enter a sentence abount 2 characters: ")

print(extract_names(sentence))



# Example usage
# scenario = "person" + "is late for class"
# google_search_api = GoogleSearchAPI()

# # Perform a Google search
# query = "reasons why " + scenario
# num_results = 10
# search_results = google_search_api.google_search(query, num_results)

# Print search results in JSON format
# print(search_results)
