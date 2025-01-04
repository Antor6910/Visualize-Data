import matplotlib.pyplot as plt
import numpy as np

# Sample data for cloud regions
regions = ['North America', 'Europe', 'Asia', 'South America', 'Australia', 'Africa']
cpu_usage = [75, 60, 90, 50, 70, 65]       # X-axis: Average CPU usage (%)
storage_utilization = [80, 70, 95, 60, 75, 68]  # Y-axis: Average storage utilization (%)
network_latency = [50, 40, 70, 90, 30, 80]  # Bubble size: Average network latency (ms)

# Normalize bubble sizes for visualization
bubble_sizes = [n * 10 for n in network_latency]

# Generate unique colors for each region
colors = np.linspace(0, 1, len(regions))

# Create the bubble chart
plt.figure(figsize=(12, 8))
scatter = plt.scatter(cpu_usage, storage_utilization, s=bubble_sizes, c=colors, cmap='cool', alpha=0.7, edgecolors='k')

# Add color bar to show region mapping
plt.colorbar(scatter, label='Region Index (0 = North America, 5 = Africa)', ticks=range(len(regions)))

# Annotate bubbles with region names
for i, region in enumerate(regions):
    plt.text(cpu_usage[i] + 1, storage_utilization[i] + 1, region, fontsize=10)

# Chart labels and title
plt.xlabel('Average CPU Usage (%)', fontsize=12)
plt.ylabel('Average Storage Utilization (%)', fontsize=12)
plt.title('Cloud Computing Infrastructure Usage Analysis', fontsize=14)
plt.grid(alpha=0.3)
plt.show()
