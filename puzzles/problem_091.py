"""
Problem 91: Given a DataFrame with a numeric column, replace all
outliers (values more than 2 standard deviations from the mean)
with the column mean.

    df = pd.DataFrame({'value': [10, 12, 11, 13, 100, 9, 11, 10, -50, 12]})
"""

import pandas as pd

df = pd.DataFrame({'value': [10, 12, 11, 13, 100, 9, 11, 10, -50, 12]})

mean = df['value'].mean()
std = df['value'].std()

print("Original:")
print(df)

df['value'] = df['value'].where(df['value'].between(mean - 2*std, mean + 2*std), mean)

print("\nAfter replacing outliers:")
print(df)
