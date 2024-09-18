
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Importing dataset
df=pd.read_excel('superstore_sales.xlsx')
#Set display options to show all colmns
pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr',False)
df.head(5)

#Last five rows of the dataset
#print(df.tail())

#shape of the dataset
#print(df.shape)

#check how many columns present in the dataset
#print(df.columns)

#A concise summary of the dataset
#print(df.info)

#Generate descriptive statistics summary
#print(df.describe().round())

#print year
#print(df.year)
year=df['year']
profit=df['profit']
plt.hist(year,profit,color='g')
plt.show()
