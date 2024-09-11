from random import random

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from EnumerateFunction import index


#step 1:Generate Random Data and write to CSV
def generate_and_ssave_data_for_pie(filename,num_categories=5):
    """
    Generate random data for a pie chart and sves it to a CSV file.
    :param filename: The name of the csv file to save data.
    :param num_categories: The name of categories for the pie chart.
    """

    #Generate random categories and values using numpy
    data={
        'Category':[f"Category{i+1}" for i in range(num_categories)],
        'Value':np.random.randint(1,100,size=num_categories)
    }

    #Create a DataFrame and save to CSV
    df=pd.DataFrame(data)
    df.to_csv(filename,index=False)

#step 2:Read data from csv file using pandas
def read_data_for_pie(filename):
    """
    Reads data from a csv file using pandas and returns it as a DataFrame
    :param filename: The name of the csv file to read data from
    :return: DataFrame with categories and values
    """
    df=pd.read_csv(filename)
    return df

#Step 3:Visualize data using a pie chart in Matplotlib
def visualize_pie_chart(df):
    """
    Visualize the data using a pie chart.
    :param df: DataFrame containg categories and values.
    """
    plt.figure(figsize=(8,8)) #set the size of the pie chart
    plt.pie(df['Value'],labels=df['Category'],autopct='%1.1f%%',startangle=140,)
    plt.title('Pie Chart of Random Data.')
    plt.axis('equal') #Equal aspects ratio ensures that pie is drawn as a circle.
    plt.show()


#Main Execution
if __name__=="__main__":
    filename='Pie_chart_data.csv'

    #Generate and save data to file
    generate_and_ssave_data_for_pie(filename)

    #Read data from file using pandas
    df=read_data_for_pie(filename)

    #Visualize the data using a pie chart
    visualize_pie_chart(df)