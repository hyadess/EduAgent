from rank_bm25 import BM25Okapi
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import pickle

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define stopwords set
stop_words = set(stopwords.words('english'))

# Remove logic gate words
logic_gate_words = {'and', 'or', 'not', 'no', 'yes'}
stop_words = stop_words - logic_gate_words  

def remove_stopwords(tokens):
    return [word for word in tokens if word.lower() not in stop_words and word.isalnum()]

# Load the tokenized documents from the pickle file

with open("./resources/bm25_with_stopwords.pkl", "rb") as f:
    tokenized_documents_with_stopwords = pickle.load(f)
with open("./resources/bm25_without_stopwords.pkl", "rb") as f:
    tokenized_documents_without_stopwords = pickle.load(f)


tokenized_content_list_with_stopwords = [doc['page_content'] for doc in tokenized_documents_with_stopwords]
tokenized_content_list_without_stopwords = [doc['page_content'] for doc in tokenized_documents_without_stopwords]


# print(tokenized_documents_with_stopwords[5])
# print(tokenized_documents_without_stopwords[5])

# Initialize BM25 with the preprocessed tokenized content
bm25_with_stopwords = BM25Okapi(tokenized_content_list_with_stopwords, k1=1.7, b=0.3)
bm25_without_stopwords = BM25Okapi(tokenized_content_list_without_stopwords, k1=1.7, b=0.3)

# print(bm25_with_stopwords.corpus_size)
# print(bm25_without_stopwords.corpus_size)

def search(query, is_stopwords_removed=True):
    tokenized_query = word_tokenize(query.lower())  # Tokenize the query
    if is_stopwords_removed:
        tokenized_query = remove_stopwords(tokenized_query)  # Remove stopwords from the query
    # print("Tokenized query: ", tokenized_query)
    if is_stopwords_removed:
        doc_scores = bm25_without_stopwords.get_scores(tokenized_query)  # Get scores for all documents

        best_doc_index = doc_scores.argmax()  # Get the index of the best matching document
        # print("Best doc index: ", best_doc_index)
        best_doc = tokenized_documents_without_stopwords[best_doc_index]  # Retrieve the best document based on the score
        # print("score: ", doc_scores[best_doc_index])
    else:
        doc_scores = bm25_with_stopwords.get_scores(tokenized_query)
        best_doc_index = doc_scores.argmax()
        # print("Best doc index: ", best_doc_index)
        best_doc = tokenized_documents_with_stopwords[best_doc_index]
        # print("score: ", doc_scores[best_doc_index])
    return {
        'image_url': best_doc['metadata']['image_url'],
        'explanation': best_doc['metadata']['explanation'],
        'score': doc_scores[best_doc_index]
    }


# ---------------------------for human evaluation---------------------------

df = pd.read_csv('../1_dataset_generation/resources/dataset.csv')
print(df.shape)

df = df[['question1', 'answer1']]

for index, row in df.iterrows():
    query = row['question1'] + '\n\n' + row['answer1']
    result = search(query, is_stopwords_removed=True)  # Search for the query and get the
    df.at[index, 'image_url'] = result['image_url']
    df.at[index, 'explanation'] = result['explanation']
    df.at[index, 'score'] = result['score']


df.to_csv('./resources/human_evaluation_retrieval.csv', index=False)








# ---------------------------for automated evaluation---------------------------


# # load the test dataset

# df = pd.read_csv("./resources/test_dataset.csv")
# print(df.shape)

# questions = df["question"].tolist()
# answers = df["answer"].tolist()
# image_urls = df["image_url"].tolist()
# print(len(questions), len(answers), len(image_urls))


# # --------------------

# retrieved_urls_with_stopwords = []
# retrieved_urls_without_stopwords = []

# total_with_stopwords = 0
# correct_with_stopwords = 0

# total_without_stopwords = 0
# correct_without_stopwords = 0


# for i in range(len(questions)):
#     question = questions[i]
#     answer = answers[i]
#     # print("Question: ", question)

#     # with stopwords

#     fetch_image_with_stopwords = search(query=question+"\n\n\n"+answer,is_stopwords_removed=False)
#     fetched_url_with_stopwords = fetch_image_with_stopwords['image_url']
#     retrieved_urls_with_stopwords.append(fetched_url_with_stopwords)
#     if fetched_url_with_stopwords == image_urls[i]:
#         correct_with_stopwords += 1
#     total_with_stopwords += 1

#     # without stopwords

#     fetch_image_without_stopwords = search(question+"\n\n\n"+answer,is_stopwords_removed=True)
#     fetched_url_without_stopwords = fetch_image_without_stopwords['image_url']
#     retrieved_urls_without_stopwords.append(fetched_url_without_stopwords)
#     if fetched_url_without_stopwords == image_urls[i]:
#         correct_without_stopwords += 1
#     total_without_stopwords += 1


# print("Accuracy with stopwords: ", correct_with_stopwords/total_with_stopwords)
# print("Accuracy without stopwords: ", correct_without_stopwords/total_without_stopwords)

# new_df_with_stopwords = pd.DataFrame()
# new_df_with_stopwords["question"] = questions
# new_df_with_stopwords["answer"] = answers
# new_df_with_stopwords["image_url"] = image_urls
# new_df_with_stopwords["retrieved_url"] = retrieved_urls_with_stopwords


# new_df_without_stopwords = pd.DataFrame()
# new_df_without_stopwords["question"] = questions
# new_df_without_stopwords["answer"] = answers
# new_df_without_stopwords["image_url"] = image_urls
# new_df_without_stopwords["retrieved_url"] = retrieved_urls_without_stopwords




# new_df_with_stopwords.to_csv("./resources/bm25_retrieves_with_stopwords.csv", index=False)
# new_df_without_stopwords.to_csv("./resources/bm25_retrieves_without_stopwords.csv", index=False)



# Accuracy with stopwords:  0.7542372881355932
# Accuracy without stopwords:  0.7627118644067796

