import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file.
# The CSV is expected to have two columns without headers:
# Example rows:
# 1833,18.930
# 1834,18.930
data = pd.read_csv('Dataset.csv', header=None, names=['Year', 'Price'])

# Create a scatter plot of the data
plt.figure(figsize=(10, 5))
plt.scatter(data['Year'], data['Price'], color='blue', label='Data Points')

plt.title('Price of gold from 1833 to 2024')
plt.xlabel('Year')
plt.ylabel('Price')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()