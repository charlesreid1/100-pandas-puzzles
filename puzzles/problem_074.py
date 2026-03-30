"""
Problem 74: Given a DataFrame, create a column that numbers each row
within its group (i.e. a row number per group).

    df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C'],
                       'value': [10, 20, 30, 40, 50, 60, 70, 80, 90]})

Expected 'row_number': [1, 2, 3, 1, 2, 1, 2, 3, 4]
"""

import pandas as pd

df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C'],
                   'value': [10, 20, 30, 40, 50, 60, 70, 80, 90]})

df['row_number'] = df.groupby('group').cumcount() + 1

print(df)
