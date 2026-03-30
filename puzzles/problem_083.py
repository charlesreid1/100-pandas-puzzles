"""
Problem 83: Given a DataFrame with a column of lists of varying
length, find the length of each list and filter to only rows where
the list has more than 2 elements.

    df = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                       'tags': [['a', 'b'], ['c'], ['d', 'e', 'f'],
                                ['g', 'h', 'i', 'j'], ['k']]})
"""

import pandas as pd

df = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                   'tags': [['a', 'b'], ['c'], ['d', 'e', 'f'],
                            ['g', 'h', 'i', 'j'], ['k']]})

df['tag_count'] = df['tags'].str.len()

print("All rows:")
print(df)

print("\nRows with more than 2 tags:")
print(df[df['tag_count'] > 2])
