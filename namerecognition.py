import spacy
import requests
from bs4 import BeautifulSoup



# Load the English language model
nlp = spacy.load("en_core_web_sm")

def extract_names(sentence):
    # Process the sentence using the language model
    doc = nlp(sentence)

    # Extract names (proper nouns) from the sentence
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    return names

# Example usage
sentence = "John and Mary went to the market with their friend Bob."
print(extract_names(sentence))


from google_search_api.google_search_api import GoogleSearchAPI


# Example usage
scenario = "person" + "is late for class"
google_search_api = GoogleSearchAPI()

# Perform a Google search
query = "reasons why " + scenario
num_results = 10
search_results = google_search_api.google_search(query, num_results)

# Print search results in JSON format
print(search_results)
