import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load the dataset
df = pd.read_csv('./resources/interactive_text_eval.csv')

# Melt the DataFrame to long format
# The 'var_name' will hold the original column names (e.g., 'openai_correctness')
# The 'value_name' will hold the scores
df_melted = df.melt(var_name='metric_model', value_name='score')

# Extract 'model' and 'metric' from the 'metric_model' column
# Using regex to capture model and metric parts
pattern = r'^(openai|llama)_(.*)$'
df_melted[['model', 'metric']] = df_melted['metric_model'].str.extract(pattern)

# Rename the 'model' column values
df_melted['model'] = df_melted['model'].replace({'openai': 'Gpt4o', 'llama': 'Llama-3.1-8B three shot'})

# Get unique metrics for plotting
unique_metrics = df_melted['metric'].unique()

# Create and save box plots for each metric
for metric in unique_metrics:
    plt.figure(figsize=(10, 7))
    # use different color palette for better visibility
    # avg line should be added in red
    sns.boxplot(x='model', y='score', data=df_melted[df_melted['metric'] == metric],
                palette="Set2", showfliers=True, flierprops=dict(marker='o', color='red', markersize=5))
    # plt.title(f'Distribution of {metric.replace("_", " ").title()} Scores by Model')
    plt.xlabel('Model')
    plt.ylabel(f'{metric.replace("_", " ").title()} Score')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'./resources/{metric}_boxplot.png')
    plt.close()