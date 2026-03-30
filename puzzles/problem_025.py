"""
Problem 25: How do you count how many unique rows a DataFrame has
(i.e. ignore all rows that are duplicates)?
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.random(size=(5, 3)))

print(len(df) - df.duplicated(keep=False).sum())

# or perhaps more simply...
print(len(df.drop_duplicates(keep=False)))
