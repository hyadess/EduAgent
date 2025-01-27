# import a csv

import pandas as pd

# read the csv file
df = pd.read_csv('../resources/test_data.csv')

# keep only the first column
df = df.iloc[:, 0]

# keep only the first 15 rows
df = df.iloc[:15]

# save the new df
df.to_csv('../resources/test_data_cleaned.csv', index=False)

