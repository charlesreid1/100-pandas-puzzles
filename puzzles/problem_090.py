"""
Problem 90: Given a DataFrame with a hierarchical column MultiIndex,
flatten the column names into a single level by joining the levels
with an underscore.

    arrays = [['score', 'score', 'info', 'info'],
              ['math', 'english', 'name', 'age']]
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples)

    df = pd.DataFrame([[90, 85, 'Alice', 25],
                       [78, 92, 'Bob', 30]],
                      columns=index)
"""

import pandas as pd

arrays = [['score', 'score', 'info', 'info'],
          ['math', 'english', 'name', 'age']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples)

df = pd.DataFrame([[90, 85, 'Alice', 25],
                   [78, 92, 'Bob', 30]],
                  columns=index)

print("Original columns:")
print(df)

df.columns = ['_'.join(col) for col in df.columns]

print("\nFlattened columns:")
print(df)
