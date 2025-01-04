# Question: Compare machine learning models based on their training time, accuracy, and dataset size.

import matplotlib.pyplot as plt

# Question: Compare machine learning models based on their training time, accuracy, and dataset size.

# Data for machine learning models
training_time = [1, 2, 3, 4]          # X-axis: Training time in hours
accuracy = [85, 90, 92, 95]           # Y-axis: Model accuracy in percentage
dataset_size = [10000, 50000, 100000, 200000]  # Bubble size: Dataset size
model_types = ['SVM', 'Random Forest', 'Neural Network', 'Logistic Regression']  # Model types

# Bubble chart
plt.figure(figsize=(10, 6))
scatter = plt.scatter(training_time, accuracy, s=[d / 1000 for d in dataset_size], c=range(len(model_types)), cmap='spring', alpha=0.6, edgecolors="w")
plt.colorbar(scatter, label='Model Type')
plt.xlabel('Training Time (hours)')
plt.ylabel('Accuracy (%)')
plt.title('Machine Learning Model Comparison')
plt.show()
