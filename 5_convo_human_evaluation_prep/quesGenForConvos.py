# inference using openai
import openai
import json
import os
import dotenv
import pandas as pd
dotenv.load_dotenv()



openai.api_key = os.getenv("OPENAI_API_KEY")
def testInference(messages):
    response = openai.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )
    return response.choices[0].message.content
    
       

# read the csv file
df = pd.read_csv('./resources/llama3.1_8b_finetuned.csv')

responses = []


question_prompt="""
The following is a piece of dialogue between a student and a teacher.\n
Ask a question based on the context and content of the dialogue as if you where an undergraduate electrical and electronic engineering student asking your professor.\n
The question should be insightful, short, and diverse.\n

You will be penalized 1999 dollars if you ask question that is same or similar to any previous question.\n
You will be penalized 2999 dollars if you provide feedback instead of a question.\n
Avoid any kind of addressing.\n\n
"""

for index, row in df.iterrows():

    messages = [
        {"role": "system", "content": question_prompt},
        {"role": "user", "content": row['question1']},
        {"role": "assistant", "content": row['answer1']},
        {"role": "user", "content": row['question2']},
        {"role": "assistant", "content": row['answer2']},
        {"role": "user", "content": row['question3']},
        {"role": "assistant", "content": row['answer3']}

    ]
    response = testInference(messages)
    responses.append(response)

# save the responses in a new column
df['question4'] = responses

# save the new df
df.to_csv('./resources/llama3.1_8b_finetuned_question4.csv', index=False)