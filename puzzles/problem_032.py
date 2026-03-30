"""
Problem 32: Implement a rolling mean over groups with window size 3,
which ignores NaN values. For example consider the following DataFrame:

    df = pd.DataFrame({'group': list('aabbabbbabab'),
                       'value': [1, 2, 3, np.nan, 2, 3,
                                 np.nan, 1, 7, 3, np.nan, 8]})

The goal is to compute the Series:

    0     1.000000
    1     1.500000
    2     3.000000
    3     3.000000
    4     1.666667
    5     3.000000
    6     3.000000
    7     2.000000
    8     3.666667
    9     2.000000
    10    4.500000
    11    4.000000

E.g. the first window of size three for group 'b' has values 3.0,
NaN and 3.0 and occurs at row index 5. Instead of being NaN the
value in the new column at this row index should be 3.0 (just the
two non-NaN values are used to compute the mean (3+3)/2)
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'group': list('aabbabbbabab'),
                   'value': [1, 2, 3, np.nan, 2, 3,
                             np.nan, 1, 7, 3, np.nan, 8]})

g1 = df.groupby(['group'])['value']              # group values
g2 = df.fillna(0).groupby(['group'])['value']    # fillna, then group values

s = g2.rolling(3, min_periods=1).sum() / g1.rolling(3, min_periods=1).count()

print(s.reset_index(level=0, drop=True).sort_index())
