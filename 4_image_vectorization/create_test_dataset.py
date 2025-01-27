import openai
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def generate_question(topic:str)->str:
    #remove image extension
    prompt = """
    Identify the theme or idea from the following text.\n
    Then generate an insightful, clear, and single line question whose answer isn't directly stated into the text but can be inferred from or connected to the text.\n

    Only reply with a complete question that can be answered without knowing what was the given text.\n

    """
    
    # Question should be slightly out of context but still related to the text.\n
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": topic},
    ]
    
    chat_completion = openai.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )
    reply = chat_completion.choices[0].message.content
    return reply


def generate_answer(question:str)->str:
    #remove image extension

    prompt = "Generate a short, precise, and accurate answer to the following query:\n\n"
    

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": question},
    ]
    
    chat_completion = openai.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )
    reply = chat_completion.choices[0].message.content
    return reply


def generate_qa_pair(topic_description:str)->str:
    question = generate_question(topic_description)
    answer = generate_answer(question)
    return question, answer


# read the csv file 
import pandas as pd
df = pd.read_csv("./resources/image_with_topic_description.csv")


# take only 5 of df
# df = df.head(50)

new_df = df[["image_url"]]

descriptions = df["topic_description"].tolist()
questions = []
answers = []
for description in descriptions:
    question, answer = generate_qa_pair(description)
    questions.append(question)
    answers.append(answer)

new_df["question"] = questions
new_df["answer"] = answers


new_df.to_csv("./resources/test_dataset.csv", index=False)