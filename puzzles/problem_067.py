"""
Problem 67: Given a DataFrame, compute the percentage change between
each row and the previous row for a numeric column. The first row
should be NaN.

    df = pd.DataFrame({'price': [100, 105, 102, 110, 108]})

Expected 'pct_change': [NaN, 0.05, -0.02857, 0.07843, -0.01818]
"""

import pandas as pd

df = pd.DataFrame({'price': [100, 105, 102, 110, 108]})

df['pct_change'] = df['price'].pct_change()

print(df)
