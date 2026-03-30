"""
Problem 87: Given a DataFrame, apply multiple aggregation functions
to a single column grouped by another column. For each group, compute
the mean, median, standard deviation, and count.

    df = pd.DataFrame({'group': list('AAABBBCCCC'),
                       'value': [10, 15, 20, 30, 25, 35, 40, 50, 45, 55]})
"""

import pandas as pd

df = pd.DataFrame({'group': list('AAABBBCCCC'),
                   'value': [10, 15, 20, 30, 25, 35, 40, 50, 45, 55]})

result = df.groupby('group')['value'].agg(['mean', 'median', 'std', 'count'])

print(result)
