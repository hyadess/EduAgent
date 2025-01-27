from rank_bm25 import BM25Okapi
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import pickle

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define the stopwords set
stop_words = set(stopwords.words('english'))

# Remove logic gate words
logic_gate_words = {'and', 'or', 'not', 'no', 'yes'}
stop_words = stop_words - logic_gate_words  


# Load the dataset
csv_file_path = './resources/image_with_topic_description.csv'
image_df = pd.read_csv(csv_file_path)

# Preprocess data with stopwords filtering
without_stopwords_data = []
with_stopwords_data = []
for index, row in image_df.iterrows():
    # Tokenize the 'topic_description' and remove stopwords
    tokenized_content_without_stopwords = [
        word.lower() for word in word_tokenize(row['topic_description'])
        if word.lower() not in stop_words and word.isalnum()  # Exclude stopwords and keep only alphanumeric tokens
    ]
    without_stopwords_data.append({
        "page_content": tokenized_content_without_stopwords,
        "metadata": {
            'topic': row['name'].split(".")[0],
            'image_url': row['image_url'],
            'explanation': row['explanation'],
        },
        "id": index
    })

    # Tokenize the 'topic_description' with stopwords
    tokenized_content_with_stopwords = [
        word.lower() for word in word_tokenize(row['topic_description'])
        if word.isalnum()  # Keep only alphanumeric tokens
    ]
    with_stopwords_data.append({
        "page_content": tokenized_content_with_stopwords,
        "metadata": {
            'topic': row['name'].split(".")[0],
            'image_url': row['image_url'],
            'explanation': row['explanation'],
        },
        "id": index
    })

# Print data insights
print(len(without_stopwords_data))
print(without_stopwords_data[0])

print(len(with_stopwords_data))
print(with_stopwords_data[0])


# Save the processed data to a pickle file
with open("./resources/bm25_without_stopwords.pkl", "wb") as f:
    pickle.dump(without_stopwords_data, f)

with open("./resources/bm25_with_stopwords.pkl", "wb") as f:
    pickle.dump(with_stopwords_data, f)