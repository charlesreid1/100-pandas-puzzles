"""
Problem 70: Given a DataFrame with a numeric column, create a new
column that bins the values into quartiles and labels them 'Q1', 'Q2',
'Q3', and 'Q4'.

    df = pd.DataFrame({'score': [15, 22, 35, 48, 55, 63, 71, 82, 90, 99]})
"""

import pandas as pd

df = pd.DataFrame({'score': [15, 22, 35, 48, 55, 63, 71, 82, 90, 99]})

df['quartile'] = pd.qcut(df['score'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

print(df)
