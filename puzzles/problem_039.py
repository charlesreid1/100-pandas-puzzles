"""
Problem 39: The From_To column would be better as two separate columns!
Split each string on the underscore delimiter `_` to give a new
temporary DataFrame with the correct values. Assign the correct column
names to this temporary DataFrame.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})

temp = df.From_To.str.split('_', expand=True)
temp.columns = ['From', 'To']

print(temp)
