"""
Problem 85: Given two DataFrames with a shared key, perform a left
join and then identify which rows from the left DataFrame had no
match in the right DataFrame.

    df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D', 'E'], 'val1': [1, 2, 3, 4, 5]})
    df2 = pd.DataFrame({'key': ['A', 'C', 'E'], 'val2': [10, 30, 50]})
"""

import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D', 'E'], 'val1': [1, 2, 3, 4, 5]})
df2 = pd.DataFrame({'key': ['A', 'C', 'E'], 'val2': [10, 30, 50]})

merged = df1.merge(df2, on='key', how='left', indicator=True)

print("Merged result:")
print(merged)

print("\nRows with no match in right DataFrame:")
print(merged[merged['_merge'] == 'left_only'])
