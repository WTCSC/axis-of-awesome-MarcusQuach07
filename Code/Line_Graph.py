import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file.
# Ensure your CSV file (e.g., "data.csv") is in the same directory as this script.
# The CSV is expected to have two columns without headers:
# Example rows:
# 1833,18.930
# 1834,18.930
data = pd.read_csv('Dataset.csv', header=None, names=['Year', 'Price'])

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(data['Year'], data['Price'], marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Price of gold from 1833 to 2024')
plt.xlabel('Year')
plt.ylabel('Price')
plt.grid(True)

# Display the plot
plt.show()