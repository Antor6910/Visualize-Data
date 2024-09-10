from matplotlib import pyplot as plt
#use the ggplot style

style.use('ggplot')

#Define two set of data
x = [16, 8, 10]
y = [8, 16, 6]
x2 = [8, 15, 11]
y2 = [6, 15, 7]

#plot the data 
plt.plot(x,y,'r',label='line one',linewidth=3)
plt.plot(x2,y2,'m',label='line two',linewidth=2)


#Add title and labels
plt.title('Epic Info')
plt.xlabel('x axis')
plt.ylabel('Y axis')

#Display legend and grid
plt.legend()

#add color in the greed
plt.grid(True,color='k')

#show the plot
plt.show()





