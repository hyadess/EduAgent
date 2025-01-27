
import numpy as np
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.retrievers import BM25Retriever, TFIDFRetriever
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()


OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")
embedding_model = OpenAIEmbeddings()
db=Chroma(embedding_function=embedding_model,persist_directory="./chroma_db")
retriever = TFIDFRetriever.load_local("./resources/tfidf_retriver.pkl",allow_dangerous_deserialization=True)

def similarity_search(query):
    # retriver=db.as_retriever()
    print(db._collection.count())
    fetched_images = db.similarity_search(query)
    print("Fetched Images: ", fetched_images)
    return fetched_images

def mmr_search(query): 
    retriver=db.as_retriever(search_type="mmr")
    fetched_images = retriver.invoke(query)
    # print(fetched_images)
    return fetched_images


def search_with_tfidf(query: str):
    """
    Perform a search using the TF-IDF retriever.
    
    Args:
        query (str): The search query.
        retriever (TFIDFRetriever): The loaded TF-IDF retriever.
        top_k (int): Number of top results to return.
    
    Returns:
        List[Document]: The retrieved documents.
    """
    results = retriever.get_relevant_documents(query)
    return results[0]



#  for automated evaluation---------------------------------------

# df = pd.read_csv("./resources/test_dataset.csv")

# questions = df["question"].tolist()
# answers = df["answer"].tolist()
# image_urls = df["image_url"].tolist()
# print(len(questions), len(answers), len(image_urls))

# total = 0
# correct = 0
# retrieved_urls = []
# for i in range(len(questions)):
#     question = questions[i]
#     answer = answers[i]
#     # print("Question: ", question)
#     fetch_image = search_with_tfidf(question+"\n\n\n"+answer)
#     # print("Fetched Images: ", fetch_images)
#     fetched_url = fetch_image.metadata['image_url']
#     retrieved_urls.append(fetched_url)
#     # print("Fetched URL: ", fetched_url)
#     # check if the fetched image is same as the image in the dataset
#     if fetched_url == image_urls[i]:
#         correct += 1
#     total += 1



# print("Accuracy: ", correct/total)

# # save in a csv file
# new_df = pd.DataFrame()
# new_df["question"] = questions
# new_df["answer"] = answers
# new_df["image_url"] = image_urls
# df["retrieved_url"] = retrieved_urls
# new_df.to_csv("./resources/tf_idf_retrieves.csv", index=False)


# Accuracy:  0.8220338983050848











