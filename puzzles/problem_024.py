"""
Problem 24: Suppose you have DataFrame with 10 columns of real
numbers, for example:

    df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))

Which column of numbers has the smallest sum? (Find that column's
label.)
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))

print(df.sum().idxmin())
