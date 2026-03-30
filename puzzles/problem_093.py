"""
Problem 93: Given a DataFrame with a column of strings, pad each
string with leading zeros so that all strings are 8 characters long.

    df = pd.DataFrame({'code': ['42', '1337', '7', '99999', '123']})

Expected 'padded': ['00000042', '00001337', '00000007', '00099999', '00000123']
"""

import pandas as pd

df = pd.DataFrame({'code': ['42', '1337', '7', '99999', '123']})

df['padded'] = df['code'].str.zfill(8)

print(df)
