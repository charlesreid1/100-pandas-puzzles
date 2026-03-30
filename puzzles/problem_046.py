"""
Problem 46: Select the labels 1, 3 and 6 from the second level of
the MultiIndexed Series.
"""

import numpy as np
import pandas as pd

letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

print(s.loc[:, [1, 3, 6]])
