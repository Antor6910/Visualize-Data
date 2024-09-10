from matplotlib import pyplot as plt  # Import the Pyplot module from Matplotlib for plotting
import numpy as np  # Import NumPy for numerical operations

# Set the plot style to 'fivethirtyeight' for a specific look and feel
plt.style.use('fivethirtyeight')

# Define the mean (mu) and standard deviation (sigma) for a normal distribution
mu = 50  # Mean of the normal distribution
sigma = 7  # Standard deviation of the normal distribution

# Generate random data from a normal (Gaussian) distribution with the specified mean and standard deviation
# 'size=200' specifies that we want 200 random values
x = np.random.normal(mu, sigma, size=200)

# Create a figure and an axes object using subplots()
fig, ax = plt.subplots()

# Plot a histogram of the random data 'x' with 20 bins and black edges for each bin
ax.hist(x, bins=20, edgecolor='black')

# Set the title of the plot
ax.set_title('Histogram')

# Set the label for the x-axis
ax.set_xlabel('Value')

# Set the label for the y-axis
ax.set_ylabel('Frequency')

# Adjust the layout of the plot to make it fit nicely within the figure area
fig.tight_layout()

# Display the plot
plt.show()

