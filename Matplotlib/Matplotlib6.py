import pandas as pd
import matplotlib.pyplot as plt

# Read the data
fifa = pd.read_csv('fifa_data.csv')

# Select the top 10 rows
fifa_data = fifa.head(10)

# Extract 'Club' and 'Overall' columns
club = fifa_data['Club'].tolist()
overall = fifa_data['Overall'].tolist()

# Create the pie chart
plt.pie(overall, labels=club, autopct='%1.1f%%')

# Display the pie chart
plt.show()
