import pandas as pd
import krippendorff
import glob
import os

# Step 1: Load all evaluator files
file_paths = glob.glob('evaluations/*.csv')  # Adjust folder as needed

dfs = []
for path in file_paths:
    evaluator = os.path.splitext(os.path.basename(path))[0]  # filename without extension
    df = pd.read_csv(path)
    df = df.rename(columns={'question1': 'datapoint_id'})
    df['evaluator'] = evaluator
    dfs.append(df)

# Step 2: Combine all data
all_data = pd.concat(dfs, ignore_index=True)

# Step 3: Melt into long format
long_df = all_data.melt(
    id_vars=['datapoint_id', 'evaluator'],
    value_vars=['correctness', 'completeness', 'conciseness'],
    var_name='metric',
    value_name='score'
)

# store the long format DataFrame for further processing
# long_df.to_csv('evaluations/long_format_evaluations.csv', index=False)


def compute_alpha(df, metric_name):
    """
    Computes Krippendorff's alpha for a given metric.
    """
    metric_df = df[df['metric'] == metric_name]

    # Pivot so each row is a datapoint, columns are evaluators
    pivot_df = metric_df.pivot(index='datapoint_id', columns='evaluator', values='score')

    # The library expects a matrix of (raters, units).
    # Our pivot table is (units, raters), so we transpose it (.T).
    # The library handles missing values (NaN) automatically.
    return krippendorff.alpha(reliability_data=pivot_df.T,
                              level_of_measurement='ordinal')

# convert the scores to numeric
long_df['score'] = pd.to_numeric(long_df['score'], errors='coerce')

# Step 5: Print alpha for each metric
for metric in ['correctness', 'completeness', 'conciseness']:
    alpha = compute_alpha(long_df, metric)
    print(f"Krippendorff's alpha for {metric}: {alpha:.4f}")
