import pandas as pd


df=pd.read_csv('../2.5_few_shot_prep/resources/all_pairs_few_shot_examples.csv')

# first randomized 30 rows
df = df.sample(n=30, random_state=1)

print(df.shape)
df.to_csv('./test_conversations/gpt4o.csv', index=False) #  test data for GPT4o


# keep only the first column named question1
df = df[['question1','example_q_1','example_a_1','example_q_2','example_a_2','example_q_3','example_a_3','example_q_4','example_a_4','example_q_5','example_a_5']]

df.to_csv('./resources/questions.csv', index=False)