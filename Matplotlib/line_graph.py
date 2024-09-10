import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10])

#for ploting dotted or dashed graph use linestyle=''
plt.plot(ypoints,linestyle='dotted')
plt.show()

plt.plot(ypoints,linestyle='dashed')
plt.show()
plt.plot(ypoints,linewidth='20.5')
plt.show()

"""
linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.
"""
