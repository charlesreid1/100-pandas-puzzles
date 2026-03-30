"""
Problem 41: Delete the From_To column from `df` and attach the
temporary DataFrame from the previous questions.
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

df = df.drop('From_To', axis=1)
df = df.join(temp)

print(df)
