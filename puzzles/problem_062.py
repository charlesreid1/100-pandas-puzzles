"""
Problem 62: Given a DataFrame of random integers, compute a new
column 'cumulative_max' that tracks the running maximum of column 'A'.

    df = pd.DataFrame({'A': [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]})

Expected result for 'cumulative_max': [3, 3, 4, 4, 5, 9, 9, 9, 9, 9]
"""

import pandas as pd

df = pd.DataFrame({'A': [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]})

df['cumulative_max'] = df['A'].cummax()

print(df)
