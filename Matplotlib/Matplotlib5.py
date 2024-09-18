from cProfile import label

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the file fifa_data.csv
fifa = pd.read_csv('fifa_data.csv')

# Initialize the figure size
plt.figure(figsize=(8, 5), dpi=100)

# Use a style
plt.style.use('ggplot')

# Convert 'Weight' column from string to integer, stripping 'lbs'
fifa['Weight'] = [int(x.strip('lbs')) if isinstance(x, str) else x for x in fifa['Weight']]
print(fifa['Weight'])

# Calculate weight categories
light = fifa.loc[fifa['Weight'] < 125].count()[0]
light_medium = fifa.loc[(fifa['Weight'] >= 125) & (fifa['Weight'] < 150)].count()[0]
medium = fifa.loc[(fifa['Weight'] >= 150) & (fifa['Weight'] < 175)].count()[0]
medium_heavy = fifa.loc[(fifa['Weight'] >= 175) & (fifa['Weight'] < 200)].count()[0]
heavy = fifa.loc[fifa['Weight'] >= 200].count()[0]

# Data for the pie chart
weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
explode = [0.4, 0.2, 0, 0, 0.4]

# Plot the pie chart
plt.title('Weight of Professional FIFA Players (lbs)')
plt.pie(weights, labels=labels, explode=explode, autopct='%1.1f%%')

# Show the plot
plt.show()


