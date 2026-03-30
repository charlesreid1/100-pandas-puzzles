"""
Problem 31: Given a DataFrame with a column of group IDs, 'grps',
and a column of corresponding integer values, 'vals', replace any
negative values in 'vals' with the group mean.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                   'vals': [12, 345, -3, 1, 45, -14, 4, 52, -54, 23, 235, -21, 57, 3, 87]})

def replace(group):
    mask = group < 0
    group[mask] = group[~mask].mean()
    return group

df['vals'] = df.groupby(['grps'])['vals'].transform(replace)

print(df)
