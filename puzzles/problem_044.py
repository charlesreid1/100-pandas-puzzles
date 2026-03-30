"""
Problem 44: Given the lists `letters = ['A', 'B', 'C']` and
`numbers = list(range(10))`, construct a MultiIndex object from the
product of the two lists. Use it to index a Series of random numbers.
Call this Series `s`.
"""

import numpy as np
import pandas as pd

letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

print(s)
