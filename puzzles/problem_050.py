"""
Problem 50: Exchange the levels of the MultiIndex so we have an index
of the form (numbers, letters). Is this new Series properly lexsorted?
If not, sort it.
"""

import numpy as np
import pandas as pd

letters = ['A', 'B', 'C']
numbers = list(range(10))

mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

new_s = s.swaplevel(0, 1)

# check
print("Is lexsorted:", new_s.index.is_monotonic_increasing)

# sort
new_s = new_s.sort_index()

print("Is lexsorted after sort:", new_s.index.is_monotonic_increasing)
print(new_s)
