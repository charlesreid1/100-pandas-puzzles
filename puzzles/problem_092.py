"""
Problem 92: Given a DataFrame, create a cross-tabulation (contingency
table) of two categorical columns.

    df = pd.DataFrame({'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'M'],
                       'handed': ['R', 'R', 'L', 'R', 'R', 'L', 'R', 'L']})
"""

import pandas as pd

df = pd.DataFrame({'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'M'],
                   'handed': ['R', 'R', 'L', 'R', 'R', 'L', 'R', 'L']})

print(pd.crosstab(df['gender'], df['handed'], margins=True))
