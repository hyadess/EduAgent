import pandas as pd
from sklearn.metrics import cohen_kappa_score
import math
from itertools import product

# ------------------------- Smart Rounding -------------------------
def best_round_pair(a, b):
    options = list(product([math.floor, math.ceil], repeat=2))
    min_diff = float('inf')
    best_a, best_b = None, None
    for f1, f2 in options:
        r1, r2 = f1(a), f2(b)
        diff = abs(r1 - r2)
        if diff < min_diff:
            min_diff = diff
            best_a, best_b = r1, r2
    return best_a, best_b

# ------------------------- Kappa Calculator -------------------------
def calculate_kappa(df_a, df_b, id_col, suffix_a, suffix_b):
    df = pd.merge(df_a, df_b, on=id_col, suffixes=(f"_{suffix_a}", f"_{suffix_b}"))

    kappa_scores = {}
    for col in ['correctness', 'completeness', 'conciseness']:
        rounded_a = []
        rounded_b = []
        for a, b in zip(df[f'{col}_{suffix_a}'], df[f'{col}_{suffix_b}']):
            ra, rb = best_round_pair(a, b)
            rounded_a.append(ra)
            rounded_b.append(rb)

        score = cohen_kappa_score(rounded_a, rounded_b, weights='quadratic')
        kappa_scores[col] = score

    return kappa_scores

# ------------------------- Load Evaluator Files -------------------------
df1 = pd.read_csv('./evaluations/evaluator_1.csv')
df2 = pd.read_csv('./evaluations/evaluator_2.csv')
df3 = pd.read_csv('./evaluations/evaluator_3.csv')
df4 = pd.read_csv('./evaluations/evaluator_4.csv')
df5 = pd.read_csv('./evaluations/evaluator_5.csv')
df6 = pd.read_csv('./evaluations/evaluator_6.csv')

# ------------------------- Compute Kappa Scores -------------------------
kappa_1_2 = calculate_kappa(df1, df2, id_col='question1', suffix_a='evaluator1', suffix_b='evaluator2')
kappa_3_4 = calculate_kappa(df3, df4, id_col='question1', suffix_a='evaluator3', suffix_b='evaluator4')
kappa_5_6 = calculate_kappa(df5, df6, id_col='question1', suffix_a='evaluator5', suffix_b='evaluator6')

# ------------------------- Print Results -------------------------
print("\nCohen's Kappa Scores (Smart Rounded, Weighted Quadratic):")
print("Evaluator 1 & 2:")
print(f"  Correctness:  {kappa_1_2['correctness']:.3f}")
print(f"  Completeness: {kappa_1_2['completeness']:.3f}")
print(f"  Conciseness:  {kappa_1_2['conciseness']:.3f}")

print("Evaluator 3 & 4:")
print(f"  Correctness:  {kappa_3_4['correctness']:.3f}")
print(f"  Completeness: {kappa_3_4['completeness']:.3f}")
print(f"  Conciseness:  {kappa_3_4['conciseness']:.3f}")

print("Evaluator 5 & 6:")
print(f"  Correctness:  {kappa_5_6['correctness']:.3f}")
print(f"  Completeness: {kappa_5_6['completeness']:.3f}")
print(f"  Conciseness:  {kappa_5_6['conciseness']:.3f}")

# ------------------------- Average Kappas -------------------------
print("\nAverage Kappa Scores across all evaluator pairs:")
print(f"  Correctness:  {sum([kappa_1_2['correctness'], kappa_3_4['correctness'], kappa_5_6['correctness']]) / 3:.3f}")
print(f"  Completeness: {sum([kappa_1_2['completeness'], kappa_3_4['completeness'], kappa_5_6['completeness']]) / 3:.3f}")
print(f"  Conciseness:  {sum([kappa_1_2['conciseness'], kappa_3_4['conciseness'], kappa_5_6['conciseness']]) / 3:.3f}")
