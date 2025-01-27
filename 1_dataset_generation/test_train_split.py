# split a csv into test and train csvs

import pandas as pd
import numpy as np
import os
import sys
import random

df=pd.read_csv('resources/dataset.csv')

# Miscellaneous Topics: 27
# Logic Gates: 22
# split the dataset into test and train where the test set is will have Miscellaneous Topics and  Logic Gates. train set will have the rest

test_df = df[(df['area'] == 'Miscellaneous Topics') | (df['area'] == 'Logic Gates')]
train_df = df[(df['area'] != 'Miscellaneous Topics') & (df['area'] != 'Logic Gates')]

print(train_df.shape)
print(test_df.shape)

train_df.to_csv('resources/train.csv',index=False)
test_df.to_csv('resources/test.csv',index=False)


# (547, 10)
# (49, 10)