"""
Problem 99: Given a DataFrame with two numeric columns, create a new
column that contains the element-wise maximum of the two columns.

    df = pd.DataFrame({'A': [5, 2, 8, 1, 9],
                       'B': [3, 7, 4, 6, 2]})

Expected 'max_AB': [5, 7, 8, 6, 9]
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [5, 2, 8, 1, 9],
                   'B': [3, 7, 4, 6, 2]})

df['max_AB'] = np.maximum(df['A'], df['B'])

# Alternative: df[['A', 'B']].max(axis=1)

print(df)
