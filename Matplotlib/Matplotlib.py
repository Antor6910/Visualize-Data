#Real world problem.different countries gas price for some year.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gas = pd.read_csv('gas_prices.csv')
print(gas)

plt.figure(figsize=(8, 5))
plt.title('Gas Price over Time (in USD)', fontdict={'fontweight': 'bold', 'fontsize': 18})

# Corrected plt.plot calls
plt.plot(gas['Year'], gas['USA'], 'b.-', label='USA')
plt.plot(gas['Year'], gas['Canada'], 'r.-', label='Canada')
plt.plot(gas['Year'], gas['South Korea'], 'g.-', label='South Korea')
plt.plot(gas['Year'], gas['Australia'], 'y.-', label='Australia')

"""
# Another way to plot many values using a loop
countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']
for country in gas.columns[1:]:  # Skipping the 'Year' column
    if country in countries_to_look_at:
        plt.plot(gas['Year'], gas[country], marker='.', label=country)

"""
"""
#if you want to add the year 2011.you can use gas['Year'][::3].to_list()+[2011]
print(gas['Year'][::3])
print(gas.columns[1:])
"""
plt.xticks(gas['Year'][::3].to_list()+[2011])
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.legend()
plt.savefig('Gas_price_figure.png', dpi=300)
plt.show()
