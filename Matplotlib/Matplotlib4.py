#pie chart of the fifa foot preference chart.
import pandas as  pd
import matplotlib.pyplot as plt
import numpy as np

fifa=pd.read_csv('fifa_data.csv')
left = (fifa['Preferred Foot'] == 'Left').sum()
#here is another way to count the right footed players count
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]


plt.figure(figsize=(8,5))

labels = ['Left', 'Right']
colors = ['#abcdef', '#aabbcc']

plt.pie([left, right], labels = labels, colors=colors, autopct='%.2f %%')

plt.title('Foot Preference of FIFA Players')

plt.show()
