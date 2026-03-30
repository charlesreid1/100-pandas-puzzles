"""
Problem 23: Given a DataFrame of numeric values, say

    df = pd.DataFrame(np.random.random(size=(5, 3)))

how do you subtract the row mean from each element in the row?
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.random(size=(5, 3)))

print(df.sub(df.mean(axis=1), axis=0))
