
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xticks

#Load the csv file data
covid_df=pd.read_csv("covid_data.csv")

#Filter COVID-19 data for the first 15 days
covid_filtered=covid_df.head(15)

#Visualize the Covid Data
plt.figure(figsize=(10,5))
plt.plot(covid_filtered['Dates'],covid_filtered['New Cases'],label='New Cases',marker='o')
plt.plot(covid_filtered['Dates'],covid_filtered['Vaccination Rates'],label='vaccination rate',linestyle='dashed')
#Customize the  plot
plt.title('COVID-19 Daily New Case')
plt.xlabel('Date')
plt.ylabel('Count/Rate')
xticks(rotation=90)
plt.legend()
plt.grid(True,axis='x')
plt.show()
