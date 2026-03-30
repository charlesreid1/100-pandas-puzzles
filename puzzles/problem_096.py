"""
Problem 96: Given a DataFrame, use the `apply` method to return the
data type of each column as a new Series.

    df = pd.DataFrame({'A': [1, 2, 3],
                       'B': [1.5, 2.5, 3.5],
                       'C': ['x', 'y', 'z'],
                       'D': [True, False, True]})
"""

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [1.5, 2.5, 3.5],
                   'C': ['x', 'y', 'z'],
                   'D': [True, False, True]})

print(df.apply(lambda col: col.dtype))
