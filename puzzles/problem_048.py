"""
Problem 48: Sum the values in `s` for each label in the first level
(you should have a Series giving you a total for labels A, B and C).
"""

import numpy as np
import pandas as pd

letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

print(s.groupby(level=0).sum())
