"""
Problem 81: Given a DataFrame with a numeric column, create a new
column that contains the rolling sum with a window of 3.

    df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

Expected 'rolling_sum': [NaN, NaN, 6, 9, 12, 15, 18, 21, 24, 27]
"""

import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

df['rolling_sum'] = df['value'].rolling(3).sum()

print(df)
