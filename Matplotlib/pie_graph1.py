import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
mylabels=["Apple","Bananna","Cherries","Dates"]
plt.title("Pie Graph")

"""
Start Angle:the default start angle is at the x-axis,but you can change the start
angle by specifying a startangle parameter.
The startangle parameter is defined with an angle in degrees,default angle is 0.

Explode->maybe you want one of the wedges to stand out?The explode parameter allows you to do that.

"""
myexplode=[0.2,0,0,0]
#use shadow
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode,shadow=True)
plt.show()
