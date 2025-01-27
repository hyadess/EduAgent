import openai
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def generate_description(image_name:str, topic_name:str)->str:
    #remove image extension
    image_name = image_name.split(".")[0]
    prompt = "describe the topic "+image_name+" in details.The topic should be described in the context of electrical and electronic engineering. Explanation of an image on that topic is also given  " +". The description should cover the usage, importance, and the impact of the algorithm, system or device described by the context and the topic name."
    

    messages = [
        {"role": "user", "content": prompt},
    ]
    
    chat_completion = openai.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    reply = chat_completion.choices[0].message.content
    return reply


# read the csv file 
import pandas as pd
df = pd.read_csv("../image_handling/resources/with_urls.csv")

# read the columns name and topic
image_names = df["name"]
explanation = df["explanation"]

# generate the description for each image and save them in a csv

descriptions = []
for i in range(len(image_names)):
    description = generate_description(image_names[i], explanation[i])
    descriptions.append(description)

df["topic_description"] = descriptions
df.to_csv("./resources/final_image_db.csv", index=False)
