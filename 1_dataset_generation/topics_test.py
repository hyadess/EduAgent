import numpy as np
import pandas as pd


df=pd.read_csv('./resources/dataset.csv')

# number of unique areas in area column and their individual counts

print(df['area'].value_counts())
print(df['topic'].value_counts())

