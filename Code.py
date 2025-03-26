import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Dataset.csv"
df = pd.read_csv(file_path)

# Inspect the first few rows to identify column names
print(df.head())

# Assuming the dataset has columns 'Year' and 'Gold Price'
# Adjust these names based on your actual column names
year_column = 'Year'
gold_price_column = 'Gold Price'

# Convert Year to an integer if it's not already
df[year_column] = df[year_column].astype(int)

# Sort by year in ascending order
df_sorted = df.sort_values(by=year_column)

# Create a line plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df_sorted[year_column], df_sorted[gold_price_column], marker='o', linestyle='-', color='gold', label='Gold Price')

# Format the plot
ax.set_xlabel("Year")
ax.set_ylabel("Price of Gold (USD)")
ax.set_title("Gold Price From 1833 to 2024")
ax.legend()

# Enable grid
ax.grid(True)

# Show interactive plot
plt.show()
