import pandas as pd
import numpy as np

#Generate COVID-19 data
dates=pd.date_range(start="2023-01-01",periods=30)
covid_data={
    "Dates":dates,
    "New Cases":np.random.randint(100,1500,len(dates)),
    "Vaccination Rates":np.linspace(50,90,len(dates))
}
covid_df=pd.DataFrame(covid_data)

#Generate Climate Data
years=np.arange(2000,2025)
climate_data={
    "Year":years,
    "Temperature Anomalies":np.random.normal(0,0.2,len(years))+0.02*(years-2000),
    "CO2 Levels": np.linspace(370, 420, len(years))  # ppm
}
climate_df=pd.DataFrame(climate_data)

#Save to the csv
covid_df.to_csv('covid_data.csv',index=False)
climate_df.to_csv('climate_data.csv',index=False)
