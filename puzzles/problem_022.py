"""
Problem 22: You have a DataFrame `df` with a column 'A' of integers.
For example:

    df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})

How do you filter out rows which contain the same integer as the row
immediately above?
"""

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})

print(df.loc[df['A'].shift() != df['A']])
