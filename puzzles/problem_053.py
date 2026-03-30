"""
Problem 53: Now create a new column for this DataFrame called
'adjacent'. This column should contain the number of mines found on
adjacent squares in the grid.

(E.g. for the first row, which is the entry for the coordinate (0, 0),
count how many mines are found on the coordinates (0, 1), (1, 0) and
(1, 1).)
"""

import numpy as np
import pandas as pd
from scipy.signal import convolve2d

X = 5
Y = 4

p = np.array(np.meshgrid(np.arange(X), np.arange(Y))).T.reshape(-1, 2)
df = pd.DataFrame(p, columns=['x', 'y'])
df['mine'] = np.random.binomial(1, 0.4, X*Y)

# Pivot to form the actual grid, use 2D convolution to count adjacent mines
mine_grid = df.pivot_table(columns='x', index='y', values='mine')
counts = convolve2d(mine_grid.astype(complex), np.ones((3, 3)), mode='same').real.astype(int)
df['adjacent'] = (counts - mine_grid).values.ravel('F')

print(df)
