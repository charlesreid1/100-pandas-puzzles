"""
Problem 45: Check the index of `s` is lexicographically sorted (this
is a necessary property for indexing to work correctly with a
MultiIndex).
"""

import numpy as np
import pandas as pd

letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

print(s.index.is_monotonic_increasing)
