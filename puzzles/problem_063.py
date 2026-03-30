"""
Problem 63: Given a DataFrame with columns 'name' and 'score',
rank each person's score in descending order (highest score gets
rank 1). Ties should receive the same rank.

    df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                       'score': [90, 85, 90, 70, 85]})
"""

import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                   'score': [90, 85, 90, 70, 85]})

df['rank'] = df['score'].rank(method='min', ascending=False).astype(int)

print(df)
