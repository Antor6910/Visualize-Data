import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the vertical and horizontal parabolas
a1, b1, c1 = 1, 0, 0  # Vertical parabola: y = a1*x^2 + b1*x + c1
a2, b2, c2 = 1, 0, 0  # Horizontal parabola: x = a2*y^2 + b2*y + c2

# Generate x values for the vertical parabola
x = np.linspace(-10, 10, 400)  # Generate 400 points between -10 and 10
y_vertical = a1 * x**2 + b1 * x + c1  # Compute y values for the vertical parabola

# Generate y values for the horizontal parabola
y = np.linspace(-10, 10, 400)  # Generate 400 points between -10 and 10
x_horizontal = a2 * y**2 + b2 * y + c2  # Compute x values for the horizontal parabola

# Create the plot
plt.figure(figsize=(8, 8))

# Plot the vertical parabola
plt.plot(x, y_vertical, label=f'Vertical Parabola: y = {a1}x^2 + {b1}x + {c1}', color='blue')

# Plot the horizontal parabola
plt.plot(x_horizontal, y, label=f'Horizontal Parabola: x = {a2}y^2 + {b2}y + {c2}', color='red')

# Configure plot details
plt.title('Vertical and Horizontal Parabolas in One Figure')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
