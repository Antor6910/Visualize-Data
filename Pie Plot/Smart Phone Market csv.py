import pandas as pd
import numpy as np

# Defining the data
companies = [
    'Company A', 'Company B', 'Company C', 'Company D', 'Company E', 
    'Company F', 'Company G', 'Company H', 'Company I', 'Company J'
]

regions = ['North America', 'Europe', 'Asia-Pacific', 'South America', 'Africa']

# Generating the dataset
np.random.seed(42)
data = {
    'Company': np.random.choice(companies, 100, replace=True),
    'Region': np.random.choice(regions, 100, replace=True),
    'Market_Share (%)': np.random.uniform(1, 20, 100),  # Random market shares
    'Revenue (in billion USD)': np.random.uniform(1, 50, 100),  # Random revenue values
    'Growth_Rate (%)': np.random.uniform(-5, 15, 100)  # Random growth rates
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Aggregating market share by company and region for pie chart visualization
#groupby ensures if Company A operates in North America and has multiple rows,they are treated as a single group.
#.agg({...}) Specifies the type of calculation(aggregation) to apply to each column in the grouped data.

aggregated_data = df.groupby(['Company', 'Region']).agg({
    'Market_Share (%)': 'sum',
    'Revenue (in billion USD)': 'sum',
    'Growth_Rate (%)': 'mean'
}).reset_index()
#.reset_index() Converts the grouped results into a new DataFrame by "flattening" the group indices into regular columns


# Saving to CSV
csv_file_path = 'smartphone_market_share.csv'
aggregated_data.to_csv(csv_file_path, index=False)
