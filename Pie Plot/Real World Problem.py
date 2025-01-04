import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
csv_file_path = 'smartphone_market_share.csv'
data = pd.read_csv(csv_file_path)

# Setting style for plots
sns.set_theme(style="whitegrid")

# 1. Pie Chart: Market Share Distribution by Region
region_data = data.groupby('Region')['Market_Share (%)'].sum()
plt.figure(figsize=(8, 6))
region_data.plot.pie(autopct='%1.1f%%', startangle=140, colormap='tab10')
plt.title('Market Share Distribution by Region')
plt.ylabel('')  # Remove y-axis label for clarity
plt.show()

# 2. Bar Plot: Revenue by Company
plt.figure(figsize=(10, 6))
company_revenue = data.groupby('Company')['Revenue (in billion USD)'].sum().sort_values(ascending=False)
sns.barplot(x=company_revenue.index, y=company_revenue.values, palette="viridis")
plt.title('Revenue by Company')
plt.xlabel('Company')
plt.ylabel('Revenue (in billion USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Scatter Plot: Revenue vs Growth Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Revenue (in billion USD)',
    y='Growth_Rate (%)',
    hue='Region',
    size='Market_Share (%)',
    sizes=(50, 300),
    data=data,
    palette="muted",
    alpha=0.7
)
plt.title('Revenue vs Growth Rate (Size by Market Share)')
plt.xlabel('Revenue (in billion USD)')
plt.ylabel('Growth Rate (%)')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 4. Heatmap: Average Market Share by Region and Company
heatmap_data = data.pivot_table(
    index='Company',
    columns='Region',
    values='Market_Share (%)',
    aggfunc='mean'
)
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='coolwarm', linewidths=.5)
plt.title('Average Market Share by Region and Company')
plt.xlabel('Region')
plt.ylabel('Company')
plt.tight_layout()
plt.show()
