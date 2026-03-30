"""
Problem 64: Given a Series of strings, extract all numeric digits
from each string and return them as integers. If there are no digits,
the value should be NaN.

    s = pd.Series(['hello123', 'world', '42abc', '7', 'no digits here'])
"""

import numpy as np
import pandas as pd

s = pd.Series(['hello123', 'world', '42abc', '7', 'no digits here'])

result = s.str.extract('(\d+)', expand=False).astype(float)

print(result)
