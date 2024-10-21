from flask import Flask, request
from flask_cors import CORS
from justificationextraction import generateReasons, extractReasons, generateSentence
from namerecognition import extract_names
import random
import time
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app) 


def parsePrompt(prompt):
    
    
    return prompt

@app.route('/characters', methods=['POST'])
def getChars():
    # Get the login credentials from the request
    data = request.get_json()
    charInfo = data['charInfo']
    promptInfo = data['promptInfo']
    
    
    print(charInfo, promptInfo)

    target = parsePrompt(promptInfo)

    resultant = target
    agents = extract_names(charInfo) 
    print(f"list of agents: {agents}")
    info = generateReasons(resultant)
    reasonsList = extractReasons(info)
    print("generating the flashback...")
    ind = random.randint(0, len(reasonsList))
    reason = reasonsList[ind]
    time.sleep(1.5)
    sentence = generateSentence(reason, resultant, agents)
    time.sleep(1.5)
    
    return [extract_names(charInfo), sentence]


if __name__ == '__main__':
    app.run(debug=True) 