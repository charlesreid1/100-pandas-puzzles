"""
Problem 79: Given a DataFrame with duplicate rows, find which rows
are duplicated (keeping the first occurrence as non-duplicate) and
display both the duplicate rows and their counts.

    df = pd.DataFrame({'A': [1, 1, 2, 3, 3, 3, 4],
                       'B': ['x', 'x', 'y', 'z', 'z', 'z', 'w']})
"""

import pandas as pd

df = pd.DataFrame({'A': [1, 1, 2, 3, 3, 3, 4],
                   'B': ['x', 'x', 'y', 'z', 'z', 'z', 'w']})

print("Duplicate rows (excluding first):")
print(df[df.duplicated()])

print("\nValue counts per unique row:")
print(df.groupby(list(df.columns)).size().reset_index(name='count'))
