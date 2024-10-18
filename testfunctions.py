from flask import Flask, request
from justificationextraction import generateReasons, extractReasons, generateSentence
from namerecognition import extract_names
import random
import time
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app) 


@app.route('/characters', methods=['POST'])
def getChars():
    # Get the login credentials from the request
    data = request.get_json()
    charInfo = data['charInfo']
    print(charInfo)
    return extract_names(charInfo)
if __name__ == '__main__':
    app.run(debug=True) 