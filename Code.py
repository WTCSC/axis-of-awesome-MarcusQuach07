import pandas as pd
from pandas_datareader import data as pdr
import matplotlib as plt
from matplotlib import pyplot as plt
from matplotlib import style
import datetime as dt

# Taking in data from 2020, January 1st
start = dt.datetime(2020, 1, 1)

# Taking in data until 2025, March 26th
end = dt.datetime(2025, 3, 26)
# Variable called Nvidia taking in pandas datareader and using yahoo to search from start to end
Nvidia = pdr.DataReader('NVDA', 'yahoo', start, end)

# Line graph style
style.use('ggplot')

# Plotting nvdias close price
Nvidia['Close'].plot(figsize=(8,8), label = 'Nvidia')

# Show line graph
plt.show()