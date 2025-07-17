# read csv into a pandas dataframe
import pandas as pd

df= pd.read_csv('../../../1_dataset_generation/resources/dataset.csv')

# print the info 
# print(df.info())

# unique values in the area column and their counts
# print(df['area'].value_counts())


# randomly sample 90 rows from the dataframe --------------------------------------------
sampled_df = df.sample(n=45, random_state=73)

# save the sampled dataframe to a new csv file
sampled_df.to_csv('./resources/sampled_dataset.csv', index=False)

# unique value count of area column in the sampled dataframe
print(sampled_df['area'].value_counts())


# divide into 3 parts ---------------------------------------------------
part1 = sampled_df.iloc[:15]
part2 = sampled_df.iloc[15:30]
part3 = sampled_df.iloc[30:]
# save each part to a separate csv file
part1.to_csv('./resources/part1.csv', index=False)
part2.to_csv('./resources/part2.csv', index=False)
part3.to_csv('./resources/part3.csv', index=False)



# each part by 2 evaluators
# 1--> eval1 and eval2
# 2--> eval3 and eval4  
# 3--> eval5 and eval6

