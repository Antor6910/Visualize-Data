from matplotlib import pyplot as plt
import numpy as np
players=['Antor','Rimi','Srizon','Upoma']

runs=[87,51,67,45]

#plot the bar graph
#here if we used barh except bar the graph will be horizontal.
plt.bar(players,runs,color='green')
plt.title("Score card")
plt.xlabel("players")
plt.ylabel("Runs")

#show the graph
plt.show()

