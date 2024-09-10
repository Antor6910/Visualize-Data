import numpy as np
import matplotlib.pyplot as plt

#set figure name
fig=plt.figure(num="sin(x) graph")
plt.xlabels("x axis")
plt.ylabels("y labels")
ax=plt.axes()

x=np.linespace(0,10,1000)
ax.plot(x,np.sin(x))

#display the graph
plt.show()

