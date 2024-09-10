import matplotlib.pyplot as plt
x=[2,2.5,3,3.5,4.5,4.7,5.0]
y=[7.5,8,8.5,9,9.5,10,10.5]

x1 = [9, 8.5, 9, 9.5, 10, 10.5, 12]
y1 = [3, 3.5, 4.7, 4, 4.5, 5, 5.2]
plt.scatter(x,y,label="HIgh income low saving",color='green')
plt.scatter(x1,y1,label="Low income high saving ",color='r')
plt.xlabel("saving*100")
plt.ylabel('Income*100')
plt.title('Scatter plot')
plt.legend()
plt.show()

