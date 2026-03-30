"""
Problem 76: Given two Series of equal length, compute the Euclidean
distance between them (treating each Series as a vector).

    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([2, 4, 6, 8, 10])
"""

import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 4, 6, 8, 10])

distance = np.sqrt(((s1 - s2) ** 2).sum())

print(f"Euclidean distance: {distance}")
