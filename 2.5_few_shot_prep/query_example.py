import tiktoken
from rank_bm25 import BM25Okapi
import joblib
import pandas as pd

tokenizer = tiktoken.get_encoding("o200k_base")

def load_tokenized_qa_pairs(filename='./resources/tokenized_qa_all_pairs.joblib'):
    return joblib.load(filename)

def tokenize_with_tiktoken(text:str):
    token_ids = tokenizer.encode(text.lower())
    return [str(token_id) for token_id in token_ids]

def get_top_5_prompts(query,filename='./resources/tokenized_qa_all_pairs.joblib'):

    tokenized_qa_pairs = load_tokenized_qa_pairs(filename)
    documents = [tokens for tokens, _, _ in tokenized_qa_pairs]
    bm25 = BM25Okapi(documents)

    tokenized_query = tokenize_with_tiktoken(query)
    scores = bm25.get_scores(tokenized_query)
    

    ranked_qa_pairs = sorted(zip(tokenized_qa_pairs, scores), key=lambda x: x[1], reverse=True)
    top_5_qa_pairs = ranked_qa_pairs[:5]

    return [(q, a) for (tokens, q, a), score in top_5_qa_pairs]


# query = "What is igbt?"
# top_5_prompts = get_top_5_prompts(query)
# for idx, (question, answer) in enumerate(top_5_prompts, 1):
#     print(f"Prompt {idx}:")
#     print(f"Q: {question}")
#     print(f"A: {answer}")
#     print()



# for only the first pair

df=pd.read_csv('../1_dataset_generation/resources/test.csv')
for question in df['question1']:
    top_5_prompts = get_top_5_prompts(question, filename='./resources/tokenized_qa_first_pairs.joblib')

    # save the top 5 prompts in the same df as example_q_1, example_a_1 and so on as columns
    for idx, (prompt_q, prompt_a) in enumerate(top_5_prompts, 1):
        df.loc[df['question1']==question, f'example_q_{idx}'] = prompt_q
        df.loc[df['question1']==question, f'example_a_{idx}'] = prompt_a

df.to_csv('./resources/first_pair_few_shot_examples.csv', index=False)


# for all the pairs
# df=pd.read_csv('../2_finetuning_and_inference_formatting/resources/test_data_shareGPT.csv')
df=pd.read_csv('../1_dataset_generation/resources/test.csv')

for question in df['question1']:
    top_5_prompts = get_top_5_prompts(question, filename='./resources/tokenized_qa_all_pairs.joblib')

    # save the top 5 prompts in the same df as example_q_1, example_a_1 and so on as columns
    for idx, (prompt_q, prompt_a) in enumerate(top_5_prompts, 1):
        df.loc[df['question1']==question, f'example_q_{idx}'] = prompt_q
        df.loc[df['question1']==question, f'example_a_{idx}'] = prompt_a

df.to_csv('./resources/all_pairs_few_shot_examples.csv', index=False)
