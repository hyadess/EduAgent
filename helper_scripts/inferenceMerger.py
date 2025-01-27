import pandas as pd


# import all csv files
test_df = pd.read_csv('../resources/test_data.csv')
reference_df = pd.read_csv('../resources/automated_eval_datasets/test_data_shareGPT.csv')
df2 = pd.read_csv('../resources/automated_eval_datasets/llama3.1_base_inference.csv')
df3 = pd.read_csv('../resources/automated_eval_datasets/llama3.1_finetune_inference.csv')
df4 = pd.read_csv('../resources/automated_eval_datasets/phi3_base_inference.csv')
df5 = pd.read_csv('../resources/automated_eval_datasets/phi3_finetune_inference.csv')


# print the length of each dataframe
# print(len(test_df))
# print(len(reference_df))
# print(len(df2))
# print(len(df3))
# print(len(df4))
# print(len(df5))


# change column name 
df2 = df2.rename(columns={"fine_tune_responses":"llama3.1_base_responses"})
df3 = df3.rename(columns={"fine_tune_responses":"llama3.1_finetune_responses"})
df4 = df4.rename(columns={"fine_tune_responses":"phi3_base_responses"})
df5 = df5.rename(columns={"fine_tune_responses":"phi3_finetune_responses"})

# print the dfs again to check

# print(df2.head())
# print(df3.head())
# print(df4.head())
# print(df5.head())


# merge all dataframes other than test_df column wise
merged_df = pd.concat([reference_df, df2, df3, df4, df5], axis=1)

# save the merged dataframe to a csv file
merged_df.to_csv('../resources/automated_eval_datasets/merged_inference.csv', index=False)

