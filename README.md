[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18839617)
# Axis of Awesome
# Data Visualization with Matplotlib and Pandas

This project contains two Python scripts for visualizing data from a CSV file that contains yearly data points and corresponding prices. The scripts leverage Python libraries such as matplotlib, pandas, and numpy to create insightful visualizations.

---

## Project Overview

The project includes two main scripts:

1. **Line Graph Script (`Line_Graph.py`):**  
   Reads a CSV file and creates a line graph with the year on the x-axis and the price on the y-axis.

2. **Scatter Plot with Line of Best Fit Script (`Scatter_Plot.py`):**  
   Reads a CSV file, creates a scatter plot of the data points, and calculates as well as plots a line of best fit using linear regression (via NumPy's polyfit).

The CSV file (e.g., `Dataset.csv`) should be formatted as follows (without headers): 1833,18.930 By year separated by a comma and then the value you like

---

## Prerequisites
Before running the scripts, ensure that you have the following installed:

- **Python 3.x**
- **Pip (Python package installer)**

### Required Python Libraries
- **pandas**
- **matplotlib**
- **numpy**

You can install these libraries via pip:

```bash
pip install pandas matplotlib numpy
```

---

## How to Run the Scripts

### 1. Line Graph Script (Line_Graph.py)

    Purpose:
    To visualize the data as a continuous line graph with markers indicating each data point.

    Steps to Run:

        Ensure dataset.csv is in the same directory as Line_Graph.py.

        Run the script using Python:

        python Line_Graph.py

    Output:
    A window will display a line graph with the x-axis representing the years and the y-axis representing the prices.

---

### 2. Scatter Plot with Best-Fit Line Script (Scatter_Plot.py)

    Purpose:
    To create a scatter plot of the data points and overlay a line of best fit calculated using linear regression.

    Steps to Run:

        Ensure Dataset.csv is in the same directory as Scatter_Plot.py.

        Run the script using Python:

    python Scatter_Plot.py

Output:
A window will display a scatter plot of the data along with a red line representing the best-fit line.

---

## Troubleshooting

    File Not Found Error:
    Ensure that the CSV file (data.csv) is correctly placed in the same directory as the scripts.

    Module Import Errors:
    Verify that all required libraries (pandas, matplotlib, numpy) are installed.

    CSV Format Issues:
    Confirm that the CSV file adheres to the expected format of two comma-separated columns without headers.

---

## Customization

    Plot Appearance:
    You can modify colors, markers, line styles, and other aesthetics by editing the matplotlib parameters in the scripts.

    Data Modifications:
    If your CSV file includes headers or additional columns, adjust the pandas.read_csv parameters accordingly.