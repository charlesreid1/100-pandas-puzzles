"""
Problem 84: Given a DataFrame with a 'timestamp' column, create new
columns for year, month, day, hour, and minute.

    df = pd.DataFrame({'timestamp': pd.to_datetime(
        ['2023-01-15 08:30:00', '2023-06-20 14:45:00',
         '2023-12-31 23:59:00', '2023-03-01 00:00:00'])})
"""

import pandas as pd

df = pd.DataFrame({'timestamp': pd.to_datetime(
    ['2023-01-15 08:30:00', '2023-06-20 14:45:00',
     '2023-12-31 23:59:00', '2023-03-01 00:00:00'])})

df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute

print(df)
