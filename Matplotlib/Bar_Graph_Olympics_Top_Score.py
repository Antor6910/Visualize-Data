import matplotlib.pyplot as plt
import numpy as np


#List of countries
countries=['USA','INDIA','China','Russia','Germany']

#Number of bronzes medals for each country
bronzes=np.array([38,17,26,19,15])

#Number of silver medals for each country
silvers=np.array([37,23,18,18,10])

#Number of gold medals for each country
golds=np.array([46,27,26,19,17])

#create a list of indices for the countries.
ind=[x for x, _ in enumerate(countries)]

#plot the gold medals bars,stacked on top of silver and brenze medals
plt.bar(ind,golds,width=0.5,label='golds',bottom=silvers+bronzes)

# Plot the silver medals bars, stacked on top of bronze medals
plt.bar(ind, silvers, width=0.5, label='silvers', color='silver', bottom=bronzes)

# Plot the bronze medals bars
plt.bar(ind, bronzes, width=0.5, label='bronzes', color='#CD853F')

# Set the x-axis ticks to the country names
plt.xticks(ind, countries)

# Label the y-axis
plt.ylabel('Medals')

# Label the x-axis
plt.xlabel("Countries")

# Add a legend to the upper right corner of the plot
plt.legend(loc="upper right")

# Set the title of the plot
plt.title("2019 Olympics Top Scores")

# Display the plot
plt.show()



