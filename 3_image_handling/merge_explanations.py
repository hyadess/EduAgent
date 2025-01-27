# python code to read two csv files and merge them into one csv file
import pandas as pd
import numpy
import os

# read the csv files
df1 = pd.read_csv('./resources/shuvo.csv')
df2 = pd.read_csv('./resources/sifat.csv')
df3 = pd.read_csv('./resources/new.csv')

# drop the topic column
df1 = df1.drop(columns=['topic'])
df2 = df2.drop(columns=['topic'])

# merge the two csv files with the same column names
df = pd.concat([df1, df2, df3], ignore_index=True)



# in the csv, there are two columns, explanations and corrected_explanations, merge them into one column such that if the corrected_explanations is not empty, then use the corrected_explanations, otherwise use the explanations
df['explanation'] = numpy.where(df['corrected_explanation'].isnull(), df['explanation'], df['corrected_explanation'])


#drop the corrected_explanation column
df = df.drop(columns=['corrected_explanation'])

# save the merged csv file
df.to_csv('./resources/merged.csv', index=False)


#size of merged csv file
print(df.shape)
