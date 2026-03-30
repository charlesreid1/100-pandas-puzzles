"""
Problem 35: For each calendar month in `s`, find the mean of values.
"""

import numpy as np
import pandas as pd

dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B')
s = pd.Series(np.random.rand(len(dti)), index=dti)

print(s.resample('M').mean())
