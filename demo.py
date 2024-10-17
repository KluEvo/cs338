from justificationextraction import generateReasons, extractReasons, generateSentence
from namerecognition import extract_names
import random
import time


def mainLoop():
    selection = 0
    resultantChoice = input("""
Selections:
1) person was late to school    
2) person fell into the swimming pool
3) person arrives at other person's house unexpectedly
""")
    while selection not in ['exit', 'quit', 'q', '']:
        options = {1: 'was late to school', 2:'fell in the swimming pool', 3: 'arrives at other person\'s house unexpectedly'}
        choice = int(resultantChoice)
        resultant = options[choice]
        agentsInf = input("character info: ")
        agents = extract_names(agentsInf) 
        print(f"list of agents: {agents}")
        info = generateReasons(resultant)
        reasonsList = extractReasons(info)
        print("generating the flashback...")
        ind = random.randint(0, len(reasonsList))
        reason = reasonsList[ind]
        time.sleep(1.5)
        sentence = generateSentence(reason, resultant, agents)
        time.sleep(1.5)
        print("\nSENTENCE:", sentence)
        resultantChoice = input("""
Selections:
1) person was late to school    
2) person fell in the swimming pool
3) person arrives at other person's house unexpectedly
""")



if __name__ == "__main__":
    mainLoop()