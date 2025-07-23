# open csvs

import pandas as pd
#----------------------------------------------------------------------------------------------

df1 = pd.read_csv('./evaluations/evaluator_1.csv')
df2 = pd.read_csv('./evaluations/evaluator_2.csv')

# for same question1, find average per row of correctness, completeness, and conciseness columns. 

avg_df1 = pd.merge(df1, df2, left_on='question1', right_on='question1', suffixes=('_evaluator1', '_evaluator2'))
avg_df1['correctness_avg'] = (avg_df1['correctness_evaluator1'] + avg_df1['correctness_evaluator2']) / 2
avg_df1['completeness_avg'] = (avg_df1['completeness_evaluator1'] + avg_df1['completeness_evaluator2']) / 2
avg_df1['conciseness_avg'] = (avg_df1['conciseness_evaluator1'] + avg_df1['conciseness_evaluator2']) / 2   
avg_df1 = avg_df1[['correctness_avg', 'completeness_avg', 'conciseness_avg']]

# save to csv
# avg_df1.to_csv('./evaluations/average_scores_1.csv', index=False)
print(len(avg_df1), "rows written to evaluations/average_scores_1.csv")


# open csvs for second set of evaluations-------------------------------------------------------

df3 = pd.read_csv('./evaluations/evaluator_3.csv')
df4 = pd.read_csv('./evaluations/evaluator_4.csv')

avg_df2 = pd.merge(df3, df4, left_on='question1', right_on='question1', suffixes=('_evaluator3', '_evaluator4'))
avg_df2['correctness_avg'] = (avg_df2['correctness_evaluator3'] + avg_df2['correctness_evaluator4']) / 2
avg_df2['completeness_avg'] = (avg_df2['completeness_evaluator3'] + avg_df2['completeness_evaluator4']) / 2
avg_df2['conciseness_avg'] = (avg_df2['conciseness_evaluator3'] + avg_df2['conciseness_evaluator4']) / 2
avg_df2 = avg_df2[['correctness_avg', 'completeness_avg', 'conciseness_avg']]
# save to csv
# avg_df2.to_csv('./evaluations/average_scores_2.csv', index=False)
print(len(avg_df2), "rows written to evaluations/average_scores_2.csv")

#----------------------------------------------------------------------------------------------

df5 = pd.read_csv('./evaluations/evaluator_5.csv')
df6 = pd.read_csv('./evaluations/evaluator_6.csv')
avg_df3 = pd.merge(df5, df6, left_on='question1', right_on='question1', suffixes=('_evaluator5', '_evaluator6'))
avg_df3['correctness_avg'] = (avg_df3['correctness_evaluator5'] + avg_df3['correctness_evaluator6']) / 2
avg_df3['completeness_avg'] = (avg_df3['completeness_evaluator5'] + avg_df3['completeness_evaluator6']) / 2
avg_df3['conciseness_avg'] = (avg_df3['conciseness_evaluator5'] + avg_df3['conciseness_evaluator6']) / 2
avg_df3 = avg_df3[['correctness_avg', 'completeness_avg', 'conciseness_avg']]
# save to csv
# avg_df3.to_csv('./evaluations/average_scores_3.csv', index=False)
# print(len(avg_df3), "rows written to evaluations/average_scores_3.csv")
#----------------------------------------------------------------------------------------------




# merge rows all three average dataframes into one 

avg_df_all = pd.concat([avg_df1, avg_df2, avg_df3], ignore_index=True)
# rename columns to remove the avg part correctness_avg -> correctness

avg_df_all.rename(columns={'correctness_avg': 'correctness',
                           'completeness_avg': 'completeness',
                           'conciseness_avg': 'conciseness'}, inplace=True)


# save to csv
# avg_df_all.to_csv('./evaluations/average_scores_all.csv', index=False)


print(len(avg_df_all), "rows written to evaluations/average_scores_all.csv")



# box plot of correctness, completeness, and conciseness averages
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12, 6))
# outliers in red dots

sns.boxplot(data=avg_df_all, palette="Set2", showfliers=True, flierprops=dict(marker='o', color='red', markersize=5))
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.savefig('./evaluations/box_plot_dataset_eval.png')

plt.show()



