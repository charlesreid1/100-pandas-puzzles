"""
Problem 68: Given two DataFrames of different lengths, perform an
outer merge on a shared key column and fill any resulting NaN values
with 0.

    df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'val1': [1, 2, 3, 4]})
    df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'val2': [5, 6, 7, 8]})
"""

import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'val1': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'val2': [5, 6, 7, 8]})

result = df1.merge(df2, on='key', how='outer').fillna(0)

print(result)
