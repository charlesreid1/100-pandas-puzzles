"""
Problem 47: Slice the Series `s`; slice up to label 'B' for the first
level and from label 5 onwards for the second level.
"""

import numpy as np
import pandas as pd

letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

print(s.loc[pd.IndexSlice[:'B', 5:]])

# or equivalently without IndexSlice...
# print(s.loc[slice(None, 'B'), slice(5, None)])
