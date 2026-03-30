"""
Problem 33: Create a DatetimeIndex that contains each business day
of 2015 and use it to index a Series of random numbers. Let's call
this Series `s`.
"""

import numpy as np
import pandas as pd

dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B')
s = pd.Series(np.random.rand(len(dti)), index=dti)

print(s.head(10))
print(f"\nLength: {len(s)}")
