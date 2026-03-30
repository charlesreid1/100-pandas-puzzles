"""
Problem 57: Columns in your DataFrame can also be used to modify
colors and sizes. Bill has been keeping track of his performance at
work over time, as well as how good he was feeling that day, and
whether he had a cup of coffee in the morning. Make a plot which
incorporates all four features of this DataFrame.

    df = pd.DataFrame({"productivity":[5,2,3,1,4,5,6,7,8,3,4,8,9],
                       "hours_in"    :[1,9,6,5,3,9,2,9,1,7,4,2,2],
                       "happiness"   :[2,1,3,2,3,1,2,3,1,2,2,1,3],
                       "caffienated" :[0,0,1,1,0,0,0,0,1,1,0,1,0]})
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.DataFrame({"productivity": [5, 2, 3, 1, 4, 5, 6, 7, 8, 3, 4, 8, 9],
                   "hours_in":     [1, 9, 6, 5, 3, 9, 2, 9, 1, 7, 4, 2, 2],
                   "happiness":    [2, 1, 3, 2, 3, 1, 2, 3, 1, 2, 2, 1, 3],
                   "caffienated":  [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0]})

df.plot.scatter("hours_in", "productivity", s=df.happiness * 30, c=df.caffienated)
plt.show()
