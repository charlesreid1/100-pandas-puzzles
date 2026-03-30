"""
Problem 52: For this DataFrame `df`, create a new column of zeros
(safe) and ones (mine). The probability of a mine occurring at each
location should be 0.4.
"""

import numpy as np
import pandas as pd

X = 5
Y = 4

p = np.array(np.meshgrid(np.arange(X), np.arange(Y))).T.reshape(-1, 2)
df = pd.DataFrame(p, columns=['x', 'y'])

# Draw samples from a binomial distribution.
df['mine'] = np.random.binomial(1, 0.4, X*Y)

print(df)
