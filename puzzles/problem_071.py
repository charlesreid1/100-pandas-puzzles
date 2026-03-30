"""
Problem 71: Given a DataFrame with a column of datetime strings,
convert them to datetime objects and extract the day of the week
name (e.g. 'Monday') into a new column.

    df = pd.DataFrame({'date': ['2023-01-02', '2023-06-15', '2023-12-25',
                                '2023-07-04', '2023-11-23']})
"""

import pandas as pd

df = pd.DataFrame({'date': ['2023-01-02', '2023-06-15', '2023-12-25',
                            '2023-07-04', '2023-11-23']})

df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()

print(df)
