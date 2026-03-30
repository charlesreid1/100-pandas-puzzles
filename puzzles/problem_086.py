"""
Problem 86: Given a DataFrame with numeric columns, normalize all
values to be between 0 and 1 (min-max normalization) per column.

    df = pd.DataFrame({'A': [10, 20, 30, 40, 50],
                       'B': [100, 200, 300, 400, 500],
                       'C': [5, 15, 25, 35, 45]})
"""

import pandas as pd

df = pd.DataFrame({'A': [10, 20, 30, 40, 50],
                   'B': [100, 200, 300, 400, 500],
                   'C': [5, 15, 25, 35, 45]})

normalized = (df - df.min()) / (df.max() - df.min())

print(normalized)
