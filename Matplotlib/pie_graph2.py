import matplotlib.pyplot as plt
import numpy as np

#set y using numpy
y=np.array([35,25,25,15])

#set labels
mylabels=(["Apple","Banna","cherries","Dates"])
#if you want to explode any portion of pie graph
myexplode=[0,0.2,0,0]

#if you want to add shadow(True)
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)

#you can add legend for better explanation
plt.legend(title="Fruits List",loc="upper right") #you can use title of the legend

plt.show()

