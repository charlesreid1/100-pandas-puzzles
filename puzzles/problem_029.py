"""
Problem 29: Consider a DataFrame `df` where there is an integer
column 'X':

    df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

For each value, count the difference back to the previous zero (or
the start of the Series, whichever is closer). These values should
therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new
column 'Y'.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

# Approach 1: using searchsorted
izero = np.r_[-1, (df['X'] == 0).nonzero()[0]]  # indices of zeros
idx = np.arange(len(df))
df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1]

print(df)

# Approach 2: using groupby/cumcount
df['Y'] = df.groupby((df['X'] == 0).cumsum()).cumcount()
# We're off by one before we reach the first zero.
first_zero_idx = (df['X'] == 0).idxmax()
df['Y'].iloc[0:first_zero_idx] += 1

print(df)
