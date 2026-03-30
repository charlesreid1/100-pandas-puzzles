"""
Problem 30: Consider a DataFrame containing rows and columns of
purely numerical data. Create a list of the row-column index
locations of the 3 largest values.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.random(size=(5, 3)))

print(df.unstack().sort_values()[-3:].index.tolist())
