import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=[0,1,2,3,4]
y=[0,2,4,6,8]

#Resize your Graph(dpi specifies pixels per inch.when saving probably should use 300 if possible
plt.figure(figsize=(8,5),dpi=100)

#Line 1
#keyword Arguements Notation
#plt.plot(x,y, lebel=2x,color='red',linewidth=2,marker='.',linestyle='--'markersize=10,markergecolor='blue')

#fmt='[color][marker][line]'
plt.plot(x,y,'b^--',label='2x')

##Line 2
#select intervals we want to plot points at
x2=np.array([0,4.5,0.5])

#plot part of the graph as line
plt.plot(x2[:6],x2[:6]**2,'r',label='x^2')

#plot remainder of graph as dor
plt.plot(x2[5:],x2[5:]**2,'r--')

# Add a title (specify font parameters with fontdict)
plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3,4,])
#plt.yticks([0,2,4,6,8,10])

# Add a legend
plt.legend()

# Save figure (dpi 300 is good when saving so graph has high resolution)
#plt.savefig('mygraph.png', dpi=300)

# Show plot
plt.show()
