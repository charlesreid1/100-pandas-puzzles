"""
Problem 88: Given a DataFrame with a column of strings, find all rows
where the string contains a pattern matching an email address.

    df = pd.DataFrame({'text': ['contact me at alice@example.com',
                                'no email here',
                                'bob@test.org is my address',
                                'call 555-1234',
                                'reach out to charlie@mail.co.uk']})
"""

import pandas as pd

df = pd.DataFrame({'text': ['contact me at alice@example.com',
                            'no email here',
                            'bob@test.org is my address',
                            'call 555-1234',
                            'reach out to charlie@mail.co.uk']})

mask = df['text'].str.contains(r'[\w.]+@[\w.]+\.\w+')

print("Rows containing an email address:")
print(df[mask])
