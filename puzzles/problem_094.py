"""
Problem 94: Given a DataFrame, compute the correlation matrix between
all numeric columns and find the pair of columns with the highest
absolute correlation (excluding self-correlations).

    df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                       'B': [5, 4, 3, 2, 1],
                       'C': [2, 4, 6, 8, 10],
                       'D': [1, 3, 2, 5, 4]})
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [5, 4, 3, 2, 1],
                   'C': [2, 4, 6, 8, 10],
                   'D': [1, 3, 2, 5, 4]})

corr = df.corr()
print("Correlation matrix:")
print(corr)

# Mask the diagonal and find the max absolute correlation
np.fill_diagonal(corr.values, 0)
max_pair = corr.abs().unstack().idxmax()
print(f"\nHighest absolute correlation: {max_pair}")
