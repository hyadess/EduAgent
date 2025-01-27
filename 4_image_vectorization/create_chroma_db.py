import numpy as np
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.retrievers import BM25Retriever, TFIDFRetriever
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv

OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")

csv_file_path = './resources/image_with_topic_description.csv'
df = pd.read_csv(csv_file_path)

data = [
    Document(
        page_content=row['topic_description'],
        metadata={
            'topic': row['name'].split(".")[0],
            'image_url': row['image_url'],
            'explanation': row['explanation'],
        },
    )
    for index, row in df.iterrows()
]

print(data[0].metadata)
print(len(data))

embedding_model = OpenAIEmbeddings()

db = Chroma.from_documents(data,embedding_model,persist_directory="./chroma_db")

tfidf_retriver = TFIDFRetriever.from_documents(data)
tfidf_retriver.save_local("./resources/tfidf_retriver.pkl")



