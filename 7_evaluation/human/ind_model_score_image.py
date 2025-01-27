import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load your CSV into a DataFrame
df = pd.read_csv("./resources/image_retrieval_evaluation.csv")
score_columns = ['relevance','understandability']

# find the averages of every score column

for column in score_columns:
    print(f"Average {column}: {df[column].mean()}")



# boxplot of the scores
plt.figure(figsize=(10, 6))

# one box per score column in one boxplot

sns.boxplot(
    data=df[score_columns],
    palette='Set2',
    showfliers=True,  # Ensure outliers are shown
    flierprops={
        'marker': 'o',
        'markerfacecolor': 'red',
        'markersize': 8,
        'linestyle': 'none'
    }  # Customize outlier marker style
)



# save the boxplot as an image
plt.savefig(f'./resources/plots/image_retrieval_scores.png')  # Save the plot as an image
plt.show()










