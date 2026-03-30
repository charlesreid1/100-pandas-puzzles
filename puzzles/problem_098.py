"""
Problem 98: Given a DataFrame, select all rows where a string column
matches one of several possible values (like SQL's IN operator) and
negate it to find rows NOT in that set.

    df = pd.DataFrame({'city': ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix',
                                'Philadelphia', 'San Antonio', 'San Diego'],
                       'pop': [8.3, 3.9, 2.7, 2.3, 1.6, 1.6, 1.5, 1.4]})
"""

import pandas as pd

df = pd.DataFrame({'city': ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix',
                            'Philadelphia', 'San Antonio', 'San Diego'],
                   'pop': [8.3, 3.9, 2.7, 2.3, 1.6, 1.6, 1.5, 1.4]})

top_3 = ['NYC', 'LA', 'Chicago']

print("Cities IN the top 3:")
print(df[df['city'].isin(top_3)])

print("\nCities NOT in the top 3:")
print(df[~df['city'].isin(top_3)])
