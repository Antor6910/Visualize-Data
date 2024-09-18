#Real world problem
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read data from fifa_data.csv file
fifa=pd.read_csv('fifa_data.csv')
#for printing first 5 data from the fifa_data.csv file
print(fifa.head(5))
bins=[40,50,60,70,80,90,100]
plt.figure(figsize=(8,5))
plt.hist(fifa.Overall,bins=bins,color='g')
plt.xticks(bins)
plt.ylabel('Number of Players')
plt.xlabel('Skil Level')
plt.title('Distribution of players Skills in FIFA 2018')
plt.show()