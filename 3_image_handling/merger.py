# merge two csv

import pandas as pd
import os

# read csv
df1 = pd.read_csv('./resources/shuvo.csv')
df2 = pd.read_csv('./resources/sifat.csv')
df3 = pd.read_csv('./resources/new.csv')

# merge csv
df1=df1[['name','explanation','corrected_explanation']]
df2=df2[['name','explanation','corrected_explanation']]
df3=df3[['name','explanation','corrected_explanation']]
df = pd.concat([df1, df2, df3], ignore_index=True)

# save csv
df.to_csv('./resources/with_wrong_explanations.csv', index=False)
print(df.shape)
