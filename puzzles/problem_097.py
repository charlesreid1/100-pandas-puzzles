"""
Problem 97: Given a DataFrame with a numeric column, compute the
exponentially weighted moving average (EWMA) with a span of 3.

    df = pd.DataFrame({'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})
"""

import pandas as pd

df = pd.DataFrame({'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})

df['ewma'] = df['value'].ewm(span=3).mean()

print(df)
