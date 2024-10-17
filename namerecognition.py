import spacy
import requests
from bs4 import BeautifulSoup
from google_search_api.google_search_api import GoogleSearchAPI

# pip install google-opensearch-api
# pip install spacy
# pip install bs4

# python -m spacy download en_core_web_sm


# Load the English language model
nlp = spacy.load("en_core_web_sm")

def extract_names(sentence):
    # Process the sentence using the language model
    doc = nlp(sentence)

    # Extract names (proper nouns) from the sentence
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    return names

# Example usage
# sentence = input("Enter a sentence abount 2 characters: ")

# print(extract_names(sentence))




# Example usage
# scenario = "person" + "is late for class"
# google_search_api = GoogleSearchAPI()

# # Perform a Google search
# query = "reasons why " + scenario
# num_results = 10
# search_results = google_search_api.google_search(query, num_results)

# Print search results in JSON format
# print(search_results)
