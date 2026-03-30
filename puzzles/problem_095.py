"""
Problem 95: Given a DataFrame with a 'date' column and a 'value'
column, resample the data to weekly frequency and compute both the
sum and the count for each week.

    dates = pd.date_range('2023-01-01', periods=30, freq='D')
    df = pd.DataFrame({'date': dates, 'value': range(30)})
"""

import pandas as pd

dates = pd.date_range('2023-01-01', periods=30, freq='D')
df = pd.DataFrame({'date': dates, 'value': range(30)})

df = df.set_index('date')

print(df.resample('W').agg(['sum', 'count']))
