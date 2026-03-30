"""
Problem 69: Given a DataFrame with a column of comma-separated values,
split each entry into separate rows while preserving the other columns.

    df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                       'skills': ['Python,R', 'Java,C++,Go', 'Python']})

Expected output should have one row per skill per person.
"""

import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                   'skills': ['Python,R', 'Java,C++,Go', 'Python']})

result = df.assign(skills=df['skills'].str.split(',')).explode('skills')

print(result)
