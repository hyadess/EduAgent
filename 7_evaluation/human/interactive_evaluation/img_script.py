import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load the dataset
df = pd.read_csv('./resources/interactive_img_eval.csv')



unique_metrics = ['relevance','understandability']

for column in unique_metrics:
    print(f"Average {column}: {df[column].mean()}")



# boxplot of the scores
plt.figure(figsize=(10, 6))

# one box per score column in one boxplot

sns.boxplot(
    data=df[unique_metrics],
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
plt.savefig(f'./resources/image_boxplot_inct.png')  # Save the plot as an image
plt.show()
