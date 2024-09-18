import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the FIFA data
fifa = pd.read_csv('fifa_data.csv')

# Prepare the plot
plt.figure(figsize=(5, 8), dpi=100)

# Retrieve 'Overall' ratings for each club
barcelona = fifa.loc[fifa['Club'] == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa['Club'] == 'Real Madrid']['Overall']
revs = fifa.loc[fifa['Club'] == 'New England Revolution']['Overall']

# Create a boxplot for the 'Overall' ratings of players from the three clubs
bp = plt.boxplot([barcelona, madrid, revs], labels=['FC Barcelona', 'Real Madrid', 'NE Revolution'],
                 patch_artist=True, medianprops={'linewidth': 2})

# Customize the boxplot appearance
for box in bp['boxes']:
    # Change outline color
    box.set(color='#4286f4', linewidth=2)
    # Change fill color
    box.set(facecolor='#e0e0e0')
    #change hatch
    box.set(hatch='o')

# Show the plot
plt.title('Boxplot of Player Ratings for Different Clubs')
plt.ylabel('Overall Ratings')
plt.show()
