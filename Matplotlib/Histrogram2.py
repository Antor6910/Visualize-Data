from matplotlib import pyplot as plt  # Import the Pyplot module from Matplotlib for plotting

# Define a list containing the ages of a population
population_age = [21, 53, 60, 49, 25, 27, 30, 42, 40, 1, 2, 102, 95, 8, 15, 105, 70, 75, 60, 52, 44, 43, 42, 45]

# Define the bins (age groups) for the histogram
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Plot the histogram for the given population age data
# 'histtype' is set to 'bar' to display the data as bars
# 'rwidth' is set to 0.8 to define the relative width of the bars
# 'color' is set to 'green' to color the bars green
plt.hist(population_age, bins, histtype='bar', rwidth=0.8, color='green')

# Set the label for the x-axis to indicate the age groups
plt.xlabel('Age Group')

# Set the label for the y-axis to indicate the number of people in each age group
plt.ylabel('Number of People')

# Set the title of the plot
plt.title("Histogram")

# Display the plot
plt.show()

