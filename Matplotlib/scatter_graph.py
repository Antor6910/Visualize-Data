from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[5,7,10]
y=[18,10,6]
x2=[6,9,11]
y2=[7,14,17]
plt.scatter(x,y,color='green')
plt.scatter(x2,y2,color='c')
plt.title("Epic Info")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
