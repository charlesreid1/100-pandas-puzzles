"""
Problem 49: Suppose that `sum()` (and other methods) did not accept a
`level` keyword argument. How else could you perform the equivalent of
`s.sum(level=1)`?
"""

import numpy as np
import pandas as pd

letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

# One way is to use .unstack()...
# This method should convince you that s is essentially
# just a regular DataFrame in disguise!
print(s.unstack().sum(axis=0))
