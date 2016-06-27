# download free end of day historical stock data
# from yahoo finance using pandas
import pandas.io.data as web
from datetime import datetime
import matplotlib.pyplot as plt
    
end = datetime.now()
start = datetime(end.year - 5, end.month, end.day)
df = web.DataReader("SPY", 'yahoo', start, end)
     
print df.tail()

import ipdb; ipdb.set_trace()


# summary statistics accross the whole DataFrame
df.describe()


import ipdb; ipdb.set_trace()


# Closing price for most recent 5 trading days
df[['Close']].tail()

# volume statistics
vol = df[['Volume']]
print "Min: %s Max: %s Average: %s" % (vol.min().values[0], vol.max().values[0], vol.mean().values[0])


import ipdb; ipdb.set_trace()


# plot the historical closing prices and volume using matplotlib
plots = df[['Close', 'Volume']].plot(subplots=True, figsize=(10, 10))
plt.show()

import ipdb; ipdb.set_trace()

# chart a basic 50 period moving average of the closing price
import pandas as pd
df['ma50'] = pd.rolling_mean(df['Close'], 50)
df['ma200'] = pd.rolling_mean(df['Close'], 200)
plots = df[['Close', 'ma50', 'ma200']].plot(subplots=False, figsize=(10, 4))
plt.show()
