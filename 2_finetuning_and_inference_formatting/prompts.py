
import pandas as pd

def extract_example(index):
    df=pd.read_csv('../1_dataset_generation/resources/train.csv')
    # extract the question from question 1 column at the given index
    question = df['question1'][index]
    answer = df['answer1'][index]

    return question, answer


def create_prompt(pair_number):
    prompt=""
    if pair_number>0:
        prompt += "## Some Examples are given below:\n\n\n"
    for i in range(pair_number):
        question, answer = extract_example(i)
        prompt += f"###Example-{i}: \nQuestion: {question}\nAnswer: {answer}\n\n"

    return prompt
    

# prompt=create_prompt(5)
# print(prompt)



