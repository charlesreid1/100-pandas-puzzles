"""
Problem 75: Given a DataFrame with a numeric column, compute the
z-score (number of standard deviations from the mean) for each value.

    df = pd.DataFrame({'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})
"""

import pandas as pd

df = pd.DataFrame({'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})

df['z_score'] = (df['value'] - df['value'].mean()) / df['value'].std()

print(df)
