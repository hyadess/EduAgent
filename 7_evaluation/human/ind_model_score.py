import pandas as pd

# Load your CSV into a DataFrame
df = pd.read_csv("./resources/text_conversation_evaluation.csv")

# Extract evaluator, conversation type, and model type from the response code
df[['evaluator', 'conversation_type', 'model_type']] = df['response_code'].str.split('_', expand=True)
df['conversation_type'] = df['conversation_type'].astype(int)
df['model_type'] = df['model_type'].astype(int)

# Group by conversation type and model type, and calculate mean scores
score_columns = ['correctness', 'conciseness', 'completeness', 'engagement']

# drop evaluator 30 and 5

#df = df.drop(df[(df['evaluator'] == '30') | (df['evaluator'] == '5')].index)




# aggregated_scores = df.groupby(['conversation_type', 'model_type'])[score_columns].mean().reset_index()

# # Save or display the results
# print(aggregated_scores)

# # Optionally, save the aggregated scores to a new CSV
# aggregated_scores.to_csv("./resources/aggregated_scores.csv", index=False)


import matplotlib.pyplot as plt
import seaborn as sns
for score in score_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        x='model_type', 
        y=score, 
        data=df, 
        palette='Set2', 
        showfliers=True,  # Ensure outliers are shown
        flierprops={
            'marker': 'o', 
            'markerfacecolor': 'red', 
            'markersize': 8,
            'linestyle': 'none'
        }  # Customize outlier marker style
    )
    # plt.title(f'Box Plot of {score.capitalize()} by Model Type (Outliers Highlighted)', fontsize=16)
    plt.xlabel('Model Type', fontsize=12)
    plt.ylabel(score.capitalize(), fontsize=12)
    plt.xticks(ticks=[0, 1, 2], labels=['GPT-4o', 'Llama3.1-8b-finetuned', 'Llama3.1-8b-fewshot'], fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f'./resources/plots/{score}.png')  # Save the plot as an image
    plt.show()