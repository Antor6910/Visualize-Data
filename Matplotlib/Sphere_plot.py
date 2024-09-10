import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting toolkit

def draw_sphere():
    # Create a new figure named "3D figure"
    fig = plt.figure("3D figure")
    
    # Add a 3D subplot to the figure; 111 means 1 row, 1 column, 1st subplot
    ax = fig.add_subplot(111, projection='3d')

    # Define the parameter u for generating points around the sphere horizontally (0 to 2*pi)
    u = np.linspace(0, 2 * np.pi, 100)
    
    # Define the parameter v for generating points vertically from the bottom to the top of the sphere (0 to pi)
    v = np.linspace(0, np.pi, 100)

    # Compute the x coordinates of the sphere's surface using the parametric equation of a sphere
    x = 1 * np.outer(np.cos(u), np.sin(v))
    
    # Compute the y coordinates of the sphere's surface
    y = 1 * np.outer(np.sin(u), np.sin(v))
    
    # Compute the z coordinates of the sphere's surface
    z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the surface of the sphere with a blue color
    ax.plot_surface(x, y, z, color='b')

    # Set the label for the X-axis
    ax.set_xlabel('X')
    
    # Set the label for the Y-axis
    ax.set_ylabel('Y')
    
    # Set the label for the Z-axis
    ax.set_zlabel('Z')

    # Display the plot
    plt.show()

# Call the function to draw the sphere
draw_sphere()

