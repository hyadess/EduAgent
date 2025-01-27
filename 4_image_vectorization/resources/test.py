#  read csv and find the length of the data

import pandas as pd

# Load the dataset

df = pd.read_csv('image_with_topic_description.csv')

# Print the length of the data

print(len(df))