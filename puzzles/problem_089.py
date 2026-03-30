"""
Problem 89: Given a DataFrame, shift a numeric column down by 1 row
and compute the difference between the original and shifted column
(i.e. a manual diff).

    df = pd.DataFrame({'value': [100, 130, 125, 150, 145, 170]})

Expected 'diff': [NaN, 30, -5, 25, -5, 25]
"""

import pandas as pd

df = pd.DataFrame({'value': [100, 130, 125, 150, 145, 170]})

df['shifted'] = df['value'].shift(1)
df['diff'] = df['value'] - df['shifted']

print(df)

# Of course, pandas has a built-in:
print("\nUsing .diff():")
print(df['value'].diff())
