import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
# Allows for pandas_datareader to be imported
# the import in the FredReader uses the wrong import change it to as below
# Moreover, you can go to FredReader file and change it but this way is easy
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

# END IMPORTS

style.use('ggplot')

# The range of the dataset
start = dt.datetime(2012, 1, 1)
end = dt.datetime.now()

df = web.DataReader('AAPL', 'robinhood', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)
df.reset_index(inplace=True)
df.drop(['interpolated', 'session'], axis=1, inplace=True) # 'Symbol' can be dropped if needed
df.rename(index=str, columns={'close_price': 'Close',
                              'high_price': 'High',
                              'low_price': 'Low',
                              'open_price': 'Open',
                              'volume': 'Volume',
                              'begins_at': 'Date'}, inplace=True)
df.set_index('Date', inplace=True)

# head(first 5 entries) or tail(last 5 entries) can be used
print(df.tail())
