"""
Problem 43: In the RecentDelays column, the values have been entered
into the DataFrame as a list. We would like each first value in its
own column, each second value in its own column, and so on. If there
isn't an Nth value, the value should be NaN.

Expand the Series of lists into a DataFrame named `delays`, rename
the columns `delay_1`, `delay_2`, etc. and replace the unwanted
RecentDelays column in `df` with `delays`.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})

delays = df['RecentDelays'].apply(pd.Series)

delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]

df = df.drop('RecentDelays', axis=1).join(delays)

print(df)
