#Import the pyplot module from Matplotlib and assign it an alias plt

from matplotlib import as pyplot plt

#Define the names of individuals
names=['Abhishek','Himanshu','Devnash']

#define the marks correspondening to each indiviual
marks=[87,76,98]

#set the size of the  entires figure to 9 inches by 3 inches
plt.figure(figsize=(9,3))

#create the first subplot in a 1x3 grid(1 row 3 coluns) and select the first plot
plt.subplot(131)

#create a bar chart with names on the x axis and marks on the y axis
plt.bar(names,marks)




#create the scatter plot with names on the x axis and marks on the y axis
plt.subplot(132)
plt.scatter(names,marks)

#create the third subplot in a 1x3 grid and select the third plot 
plt.suplot(133)

#create a line plot with names on the x axis and marks on the y axis
plt.plot(names,marks)

#Add a super title to the entire figure
plt.title('Catagorical ploting')

#Render the figure and display the plots
plt.show()





