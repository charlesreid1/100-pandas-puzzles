"""
Problem 51: Let's suppose we're playing Minesweeper on a 5 by 4 grid,
i.e. X = 5, Y = 4. To begin, generate a DataFrame `df` with two
columns, 'x' and 'y' containing every coordinate for this grid. That
is, the DataFrame should start:

   x  y
0  0  0
1  0  1
2  0  2
"""

import numpy as np
import pandas as pd

X = 5
Y = 4

p = np.array(np.meshgrid(np.arange(X), np.arange(Y))).T.reshape(-1, 2)
df = pd.DataFrame(p, columns=['x', 'y'])

print(df)
