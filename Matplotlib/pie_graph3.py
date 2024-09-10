from matplotlib import pyplot as plt
import numpy as np

#List of players
players=['Rohit','Virat','Shikar','Yuvraj']

#Number of runs in each players
Runs=[45,30,15,10]

#Explode the first slice.it create space between two color intersection
explode=(0,0,0.1,0)

#Create a figure and set of subplots
fig1,ax1=plt.subplots()

#plot a pie chart
"""
autopct: A common use of autopct is with a format string that specfies how the percentage should be displayed and % function define how many digit print after the decimal value.
"""
ax1.pie(Runs,explode=explode,labels=players,autopct='%1.1f%%',shadow=True,startangle=90)

#Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

#Display the plot
plt.show()

