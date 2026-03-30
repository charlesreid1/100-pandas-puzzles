"""
Problem 77: Given a DataFrame, find all columns where more than 25%
of the values are NaN.

    df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                       'B': [np.nan, np.nan, np.nan, 4],
                       'C': [1, 2, 3, 4],
                       'D': [np.nan, 2, np.nan, np.nan]})
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [np.nan, np.nan, np.nan, 4],
                   'C': [1, 2, 3, 4],
                   'D': [np.nan, 2, np.nan, np.nan]})

pct_null = df.isnull().mean()
print("Percent null per column:")
print(pct_null)

print("\nColumns with >25% NaN:")
print(pct_null[pct_null > 0.25].index.tolist())
