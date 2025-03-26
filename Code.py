import pandas as pd
import matplotlib as plt
import numpy as np

x, y = np.loadtxt('Dataset.csv',
                  unpack=True,
                  delimiter=',')

plt.plot(x,y)

plt.title('Value of Gold From 1833 to 2024')
plt.xlabel('Years')
plt.ylabel('Value in USD')

plt.show()