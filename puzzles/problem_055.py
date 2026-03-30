"""
Problem 55: Finally, convert the DataFrame to a grid of the adjacent
mine counts: columns are the x coordinate, rows are the y coordinate.
"""

import numpy as np
import pandas as pd
from scipy.signal import convolve2d

X = 5
Y = 4

p = np.array(np.meshgrid(np.arange(X), np.arange(Y))).T.reshape(-1, 2)
df = pd.DataFrame(p, columns=['x', 'y'])
df['mine'] = np.random.binomial(1, 0.4, X*Y)

mine_grid = df.pivot_table(columns='x', index='y', values='mine')
counts = convolve2d(mine_grid.astype(complex), np.ones((3, 3)), mode='same').real.astype(int)
df['adjacent'] = (counts - mine_grid).values.ravel('F')
df.loc[df['mine'] == 1, 'adjacent'] = np.nan

print(df.drop('mine', axis=1).set_index(['y', 'x']).unstack())
