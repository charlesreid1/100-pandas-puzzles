"""
Problem 100: Given a DataFrame, write it to a CSV file without the
index, read it back in, and verify that the round-tripped DataFrame
is equal to the original.

    df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                       'age': [25, 30, 35],
                       'score': [90.5, 85.0, 92.3]})
"""

import os
import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                   'age': [25, 30, 35],
                   'score': [90.5, 85.0, 92.3]})

# Write to CSV
df.to_csv('/tmp/problem_100.csv', index=False)

# Read back
df_read = pd.read_csv('/tmp/problem_100.csv')

# Verify
print("Original:")
print(df)
print("\nRound-tripped:")
print(df_read)
print(f"\nDataFrames are equal: {df.equals(df_read)}")

# Clean up
os.remove('/tmp/problem_100.csv')
