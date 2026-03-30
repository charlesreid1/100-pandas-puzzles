"""
Problem 72: Given a DataFrame, pivot it from long format to wide
format and then melt it back to long format.

    df = pd.DataFrame({'student': ['Alice', 'Alice', 'Bob', 'Bob'],
                       'subject': ['Math', 'English', 'Math', 'English'],
                       'grade': [90, 85, 78, 92]})
"""

import pandas as pd

df = pd.DataFrame({'student': ['Alice', 'Alice', 'Bob', 'Bob'],
                   'subject': ['Math', 'English', 'Math', 'English'],
                   'grade': [90, 85, 78, 92]})

# Pivot to wide
wide = df.pivot(index='student', columns='subject', values='grade')
print("Wide format:")
print(wide)

# Melt back to long
long = wide.reset_index().melt(id_vars='student', var_name='subject', value_name='grade')
print("\nLong format:")
print(long)
