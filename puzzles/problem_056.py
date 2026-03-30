"""
Problem 56: Pandas is highly integrated with the plotting library
matplotlib. For starters, make a scatter plot of this random data,
but use black X's instead of the default markers.

    df = pd.DataFrame({"xs":[1,5,2,8,1], "ys":[4,2,1,9,6]})
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.DataFrame({"xs": [1, 5, 2, 8, 1], "ys": [4, 2, 1, 9, 6]})

df.plot.scatter("xs", "ys", color="black", marker="x")
plt.show()
