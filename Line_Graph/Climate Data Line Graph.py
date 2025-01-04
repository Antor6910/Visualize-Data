import matplotlib.pyplot as plt
import pandas as pd

#Load the Climate data file
climate_df=pd.read_csv('climate_data.csv')

#filter the first 10 row from the data set
climate_filtered=climate_df.head(10)

# Climate Change Visualization
plt.figure(figsize=(10, 5))
plt.plot(climate_filtered['Year'], climate_filtered['Temperature Anomalies'], label="Temperature Anomalies", color="orange",marker='o')
plt.plot(climate_filtered['Year'], climate_filtered['CO2 Levels'], label="CO2 Levels", linestyle="--", color="green",marker='o')
plt.title("Climate Change: Temperature Anomalies and CO2 Levels")
plt.xlabel("Year")
plt.ylabel("Anomaly/CO2 Levels")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()
