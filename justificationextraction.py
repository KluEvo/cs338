from mistralai import Mistral
import re
from transformers import pipeline
import random

import time

api_key = "COPY THIS FROM ELSEWHERE"

model = "open-mistral-7b"
client = Mistral(api_key=api_key)

def getMistralInfo():
    return model, client


actor = "John"
resultant = "be late to school"
def generateReasons(resultant):
    model, client = getMistralInfo()
    chat_response = client.chat.complete(
        model=model,
        messages=[{"role":"user", "content":f"list reasons why a person {resultant}?"}]
    )
    info = chat_response.choices[0].message.content
    return info


# info = """
# Detention is a form of disciplinary action taken in educational institutions, workplaces, and sometimes in legal settings. The reasons for someone being sent to detention can vary depending on the specific rules and regulations of the institution or organization. Here are some common reasons why people might go to detention:

# 1. Lateness or Tardiness: Arriving at school or work after the designated start time without a valid excuse can result in detention.

# 2. Absenteeism: Frequent absenteeism or unexplained absences from school or work can lead to detention or other disciplinary actions.

# 3. Academic Misconduct: Cheating on tests, plagiarizing assignments, or other forms of academic dishonesty can result in detention.

# 4. Disruptive Behavior: Acting out in class, causing disturbances in the classroom or school, or engaging in behavior that disrupts the learning environment can lead to detention.

# 5. Physical Violence or Threats: Physical violence or threats of violence towards other students, teachers, or staff can result in detention and potentially more severe disciplinary actions.

# 6. Cyberbullying: Bullying or harassing others through electronic means can lead to detention and possible legal consequences.

# 7. Theft or Property Damage: Stealing property from others or damaging property can result in detention.

# 8. Dress Code Violations: Failing to adhere to the dress code, such as wearing inappropriate clothing or accessories, can lead to detention.

# 9. Breaking School Rules: Violating other school rules, such as those related to smoking, vaping, or use of electronic devices during class, can result in detention.

# 10. Failure to Complete Assignments: Not completing assigned work or tasks can lead to detention, especially if it is a repeated offense."""




def extractReasons(info):
    # Extract reasons using regular expressions
    pattern = r'\d+\.\s*(.*?)(?=\n\d+\.|$)'
    reasonsList = re.findall(pattern, info, re.DOTALL)

    # Clean up the reasons
    reasonsList = [reason.strip() for reason in reasonsList]
    return reasonsList

# Generate a sentence using GPT-2
def generateSentence(reason, resultant, actor):
    prompt = f"{actor} {resultant} because {reason}."
    
    model, client = getMistralInfo()
    chat_response = client.chat.complete(
        model=model,
        messages=[{"role":"user", "content":f"give a short, 1 sentence, silly description of {prompt}. No need to do a conclusion or be too verbose"}]
    )
    info = chat_response.choices[0].message.content
    # print(chat_response.choices[0].message.content)


    return info

# Generate and print a sentence for each reason

if __name__ == "__main__":
    info = generateReasons(resultant)
    reasonsList = extractReasons(info)
    time.sleep(5)
    reason = reasonsList[random.randint(0, len(reasonsList))]
    sentence = generateSentence(reason)
    print("\nSENTENCE:", sentence)

