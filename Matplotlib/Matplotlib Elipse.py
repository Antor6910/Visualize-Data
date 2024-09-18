import numpy as np
import matplotlib.pyplot as plt

#parameters for the ellipse
h=0 #x-coordinates of the center
k=0 #y-coordinates of the center
a=5 #length of semi major axis
b=3 #length  of semi minor axis

#Generate values for the parameters t
t=np.linspace(0,2*np.pi,400)

#Parameters equations for the ellipse
x=h+a*np.cos(t)
y=k+np.sin(t)

#Create the plot
plt.figure(figsize=(8,8))
plt.plot(x,y,label=f'Ellipse:center=({h},{k}) a={a},b={b}',color='blue')

#configure plot details
plt.title('Ellipse plot')
plt.xlabel('x axis')
plt.ylabel('Y axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.axis('equal')  # Ensure the aspect ratio is equal so the ellipse is not skewed
plt.show()