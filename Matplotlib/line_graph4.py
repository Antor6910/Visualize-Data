# Importing the required libraries for plotting and numerical operations
import matplotlib.pyplot as plt
import numpy as np

# Creating arrays for the x and y coordinates
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])  # x-coordinates for the scatter plot
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])  # y-coordinates for the scatter plot

# Array defining the sizes of each point in the scatter plot
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# Array defining the colors of each point in the scatter plot
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# Creating a scatter plot with specified colors and sizes for each point
# 'c=colors' sets the color for each point; 'cmap' applies a colormap; 's=sizes' sets the size of each point; 'alpha' sets the transparency level
plt.scatter(x, y, c=colors, cmap='viridis', s=sizes, alpha=1)

# Displaying a color bar, which is a key for the color mapping in the scatter plot
plt.colorbar()

# Showing the first scatter plot
plt.show()

# Generating random x and y coordinates for the second scatter plot
x = np.random.randint(100, size=(100))  # Random x-coordinates between 0 and 100 for 100 points
y = np.random.randint(100, size=(100))  # Random y-coordinates between 0 and 100 for 100 points

# Generating random color values for each point in the scatter plot
colors = np.random.randint(100, size=(100))  # Random color values between 0 and 100 for 100 points

# Creating a second scatter plot with random data
# 'c=colors' sets the color for each point; 'alpha=0.5' sets the transparency; 'cmap' specifies the colormap
plt.scatter(x, y, c=colors, alpha=0.5, cmap='nipy_spectral')

# Displaying a color bar for the second scatter plot
plt.colorbar()

# Showing the second scatter plot
plt.show()

