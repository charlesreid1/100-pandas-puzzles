"""
Problem 61: Create a DataFrame with 1000 rows and two columns: 'A'
containing random integers from 1 to 10 and 'B' containing random
floats. For each unique value in 'A', find the row index of the
maximum value in 'B'.
"""

import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame({'A': np.random.randint(1, 11, 1000),
                   'B': np.random.random(1000)})

print(df.loc[df.groupby('A')['B'].idxmax()])
