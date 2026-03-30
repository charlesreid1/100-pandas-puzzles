"""
Problem 80: Given a DataFrame with columns 'category' and 'value',
compute each value as a percentage of its category's total.

    df = pd.DataFrame({'category': ['A', 'A', 'A', 'B', 'B'],
                       'value': [10, 20, 30, 40, 60]})

Expected 'pct_of_group': for A: [16.67, 33.33, 50.0], for B: [40.0, 60.0]
"""

import pandas as pd

df = pd.DataFrame({'category': ['A', 'A', 'A', 'B', 'B'],
                   'value': [10, 20, 30, 40, 60]})

df['pct_of_group'] = df['value'] / df.groupby('category')['value'].transform('sum') * 100

print(df)
