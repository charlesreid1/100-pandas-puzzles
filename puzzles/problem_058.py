"""
Problem 58: What if we want to plot multiple things? Pandas allows you
to pass in a matplotlib Axis object for plots, and plots will also
return an Axis object.

Make a bar plot of monthly revenue with a line plot of monthly
advertising spending (numbers in millions).

    df = pd.DataFrame({"revenue":[57,68,63,71,72,90,80,62,59,51,47,52],
                       "advertising":[2.1,1.9,2.7,3.0,3.6,3.2,2.7,2.4,1.8,1.6,1.3,1.9],
                       "month":range(12)})
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.DataFrame({"revenue": [57, 68, 63, 71, 72, 90, 80, 62, 59, 51, 47, 52],
                   "advertising": [2.1, 1.9, 2.7, 3.0, 3.6, 3.2, 2.7, 2.4, 1.8, 1.6, 1.3, 1.9],
                   "month": range(12)})

ax = df.plot.bar("month", "revenue", color="green")
df.plot.line("month", "advertising", secondary_y=True, ax=ax)
ax.set_xlim((-1, 12))
plt.show()
