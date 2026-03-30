"""
Problem 26: You have a DataFrame that consists of 10 columns of
floating-point numbers. Suppose that exactly 5 entries in each row
are NaN values. For each row of the DataFrame, find the column which
contains the third NaN value.

(You should return a Series of column labels.)
"""

import numpy as np
import pandas as pd

nan = np.nan
data = [[0.04, nan, nan, 0.25, nan, 0.43, 0.71, 0.51, nan, nan],
        [nan, nan, nan, 0.04, 0.76, nan, nan, 0.67, 0.76, 0.16],
        [nan, nan, 0.5, nan, 0.31, 0.37, nan, nan, 0.57, 0.12],
        [0.27, nan, 0.73, 0.33, nan, nan, 0.43, nan, 0.12, nan],
        [nan, nan, nan, 0.41, 0.85, nan, nan, 0.48, 0.57, 0.12]]

df = pd.DataFrame(data, columns=list('abcdefghij'))

print((df.isnull().cumsum(axis=1) == 3).idxmax(axis=1))
