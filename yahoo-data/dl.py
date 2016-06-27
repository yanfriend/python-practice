import pandas
import pandas.io.data as web
from datetime import datetime

tickers = ['^gspc']
start = datetime(2015,1,1)
end = datetime(2016,1,1)
stockRawData = web.DataReader(tickers, 'yahoo', start, end)
print stockRawData.to_frame()

import ipdb; ipdb.set_trace()

sliceKey = 'Adj Close'
adjCloseData = stockRawData.ix[sliceKey]
print adjCloseData

import ipdb; ipdb.set_trace()

ibmAdjCloseData = adjCloseData['^gspc']
print ibmAdjCloseData


