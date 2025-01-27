import tiktoken
from rank_bm25 import BM25Okapi
import joblib
import pandas as pd

tokenizer = tiktoken.get_encoding("o200k_base")

def read_first_qa_from_csv():
    df = pd.read_csv("../1_dataset_generation/resources/train.csv")
    qa_pairs = list(zip(df['question1'], df['answer1']))
    print("only first pair:",len(qa_pairs))
    return qa_pairs

def read_all_qa_from_csv():
    df = pd.read_csv("../1_dataset_generation/resources/train.csv")
    # list every pair of question and answer
    qa_pairs = (
        list(zip(df['question1'], df['answer1'])) +
        list(zip(df['question2'], df['answer2'])) +
        list(zip(df['question3'], df['answer3'])) +
        list(zip(df['question4'], df['answer4']))
    )
    print("all pairs:", len(qa_pairs))
    return qa_pairs


def tokenize_with_tiktoken(text:str):
    token_ids = tokenizer.encode(text.lower())
    return [str(token_id) for token_id in token_ids]

qa_first_pairs = read_first_qa_from_csv()
qa_all_pairs = read_all_qa_from_csv()

tokenized_qa_first_pairs = [(tokenize_with_tiktoken(q + " " + a), q, a) for q, a in qa_first_pairs]
tokenized_qa_all_pairs = [(tokenize_with_tiktoken(q + " " + a), q, a) for q, a in qa_all_pairs]

joblib.dump(tokenized_qa_all_pairs, './resources/tokenized_qa_all_pairs.joblib', compress=3)
joblib.dump(tokenized_qa_first_pairs, './resources/tokenized_qa_first_pairs.joblib', compress=3)