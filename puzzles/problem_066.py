"""
Problem 66: Given a DataFrame with columns 'group', 'date', and
'value', find the row with the most recent date for each group.

    df = pd.DataFrame({
        'group': ['A', 'A', 'B', 'B', 'A', 'B'],
        'date': pd.to_datetime(['2020-01-01', '2020-03-15', '2020-02-10',
                                '2020-04-20', '2020-02-28', '2020-01-05']),
        'value': [10, 20, 30, 40, 50, 60]
    })
"""

import pandas as pd

df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'A', 'B'],
    'date': pd.to_datetime(['2020-01-01', '2020-03-15', '2020-02-10',
                            '2020-04-20', '2020-02-28', '2020-01-05']),
    'value': [10, 20, 30, 40, 50, 60]
})

print(df.loc[df.groupby('group')['date'].idxmax()])
