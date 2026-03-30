"""
Problem 42: In the Airline column, you can see some extra punctuation
and symbols have appeared around the airline names. Pull out just the
airline name. E.g. '(British Airways. )' should become 'British Airways'.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})

df['Airline'] = df['Airline'].str.extract('([a-zA-Z\\s]+)', expand=False).str.strip()

print(df['Airline'])
