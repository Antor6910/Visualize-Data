import numpy as np
#import matplotlib
from matplotlib import pyplot as plt

xpoints=np.array([1,4,8])
ypoints=np.array([3,7,10])

#plot xpoints and ypoints and use marker,color
plt.plot(xpoints,ypoints,'o',marker='*',linewidth=5,label='line graph')


plt.legend()

#display the graph
plt.show()


