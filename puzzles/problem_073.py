"""
Problem 73: Given a DataFrame with missing values, forward-fill NaNs
within each group independently.

    df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B', 'B'],
                       'value': [1, np.nan, np.nan, 10, np.nan, 30]})

Expected 'value' after fill: [1, 1, 1, 10, 10, 30]
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B', 'B'],
                   'value': [1, np.nan, np.nan, 10, np.nan, 30]})

df['value'] = df.groupby('group')['value'].ffill()

print(df)
