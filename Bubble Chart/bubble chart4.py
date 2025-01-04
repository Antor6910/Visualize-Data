import matplotlib.pyplot as plt
import numpy as np

# Sample data for customer segments
segments = ['Premium', 'Regular', 'Occasional', 'Low-value']
purchase_frequency = [50, 20, 10, 5]        # X-axis: Purchases per year
avg_transaction_value = [200, 100, 50, 30]  # Y-axis: Average transaction value (USD)
customer_lifetime_value = [10000, 5000, 1500, 500]  # Bubble size: CLV (USD)

# Normalize bubble sizes for visualization
bubble_sizes = [clv / 10 for clv in customer_lifetime_value]

# Generate unique colors for each segment
colors = np.linspace(0, 1, len(segments))

# Create the bubble chart
plt.figure(figsize=(12, 8))
scatter = plt.scatter(purchase_frequency, avg_transaction_value, s=bubble_sizes, c=colors, cmap='plasma', alpha=0.7, edgecolors='k')

# Add color bar to show segment mapping
plt.colorbar(scatter, label='Segment Index (0 = Premium, 3 = Low-value)', ticks=range(len(segments)))

# Annotate bubbles with segment names
for i, segment in enumerate(segments):
    plt.text(purchase_frequency[i] + 1, avg_transaction_value[i] + 1, segment, fontsize=10)

# Chart labels and title
plt.xlabel('Purchase Frequency (Purchases per Year)', fontsize=12)
plt.ylabel('Average Transaction Value (USD)', fontsize=12)
plt.title('Customer Segmentation in E-Commerce', fontsize=14)
plt.grid(alpha=0.3)
plt.show()
