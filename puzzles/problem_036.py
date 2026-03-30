"""
Problem 36: For each group of four consecutive calendar months in `s`,
find the date on which the highest value occurred.
"""

import numpy as np
import pandas as pd

dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B')
s = pd.Series(np.random.rand(len(dti)), index=dti)

print(s.groupby(pd.Grouper(freq='4M')).idxmax())
