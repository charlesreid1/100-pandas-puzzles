"""
Problem 37: Create a DateTimeIndex consisting of the third Thursday
in each month for the years 2015 and 2016.
"""

import pandas as pd

print(pd.date_range('2015-01-01', '2016-12-31', freq='WOM-3THU'))
