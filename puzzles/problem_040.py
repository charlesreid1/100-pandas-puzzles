"""
Problem 40: Notice how the capitalisation of the city names is all
mixed up in this temporary DataFrame. Standardise the strings so that
only the first letter is uppercase (e.g. "londON" should become
"London".)
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

temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()

print(temp)
