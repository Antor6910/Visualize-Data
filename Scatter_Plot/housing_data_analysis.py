import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
data=pd.read_csv('housing_data.csv')

#show the first few rows of the dataset
print(data.head())

#Perform basic statistical analysis
print(data.describe())

#Check for missing values
print(data.isnull().sum())

#Visualize the relationships using scatter plots
sns.pairplot(data[['Square_Feet', 'Bedrooms', 'House_Age', 'Proximity_to_Schools_km', 'Proximity_to_Parks_km', 'Price']])
plt.show()

# Scatter plot: Square footage vs Price
plt.figure(figsize=(8,6))
plt.scatter(data['Square_Feet'], data['Price'], color='blue', alpha=0.5)
plt.title('Square Footage vs Price')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Scatter plot: Number of bedrooms vs Price
plt.figure(figsize=(8,6))
plt.scatter(data['Bedrooms'], data['Price'], color='green', alpha=0.5)
plt.title('Bedrooms vs Price')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')
plt.show()

#Correlation matrix to check relationships
corr=data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr,annot=True,cmap='coolwarm',linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()
