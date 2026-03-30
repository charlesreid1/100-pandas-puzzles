"""
Problem 65: Given a DataFrame, replace all values greater than the
column mean with the string 'high' and all others with 'low'.

    df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])
"""

import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])

print("Original:")
print(df)

result = df.where(df > df.mean(), 'low').where(df <= df.mean(), 'high')

print("\nResult:")
print(result)
