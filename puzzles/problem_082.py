"""
Problem 82: Given a DataFrame, transpose it so that rows become
columns and columns become rows, while preserving the original
column names as the new index.

    df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                       'age': [25, 30, 35],
                       'city': ['NYC', 'LA', 'Chicago']})
"""

import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                   'age': [25, 30, 35],
                   'city': ['NYC', 'LA', 'Chicago']})

print("Original:")
print(df)

print("\nTransposed:")
print(df.set_index('name').T)
