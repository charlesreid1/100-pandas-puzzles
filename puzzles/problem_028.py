"""
Problem 28: A DataFrame has two integer columns 'A' and 'B'. The
values in 'A' are between 1 and 100 (inclusive). For each group of
10 consecutive integers in 'A' (i.e. (0, 10], (10, 20], ...),
calculate the sum of the corresponding values in column 'B'.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'A': np.random.randint(1, 101, 100),
                   'B': np.random.randint(1, 101, 100)})

print(df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum())
