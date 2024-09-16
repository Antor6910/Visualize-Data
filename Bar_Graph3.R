
library(ggplot2)

# Create a dataset for all graphs
data <- data.frame(
  category = c("A", "B", "C", "D"),
  values = c(10, 23, 17, 9),
  group = c("X", "X", "Y", "Y")  # For grouped bar chart
)

# 1. Simple Bar Graph with Custom Colors
ggplot(data, aes(x = category, y = values)) +
  geom_bar(stat = "identity", fill = "lightblue") +  # Bar plot with identity stat
  xlab("Category") +  # X-axis label
  ylab("Values") +  # Y-axis label
  ggtitle("Simple Bar Graph") +  # Title
  theme_minimal()  # Minimal theme


# 2. Grouped Bar Graph
ggplot(data, aes(x = category, y = values, fill = group)) +
  geom_bar(stat = "identity", position = "dodge") +  # Grouped bar with dodge position
  xlab("Category") +  # X-axis label
  ylab("Values") +  # Y-axis label
  ggtitle("Grouped Bar Graph") +  # Title
  scale_fill_manual(values = c("X" = "red", "Y" = "blue")) +  # Custom color for groups
  theme_classic()  # Classic theme


# 3. Bar Graph with Horizontal Bars
ggplot(data, aes(x = category, y = values)) +
  geom_bar(stat = "identity", fill = "darkgreen") +  # Standard bar plot
  xlab("Category") +  # X-axis label
  ylab("Values") +  # Y-axis label
  ggtitle("Horizontal Bar Graph") +  # Title
  coord_flip() +  # Flip coordinates for horizontal bars
  theme_light()  # Light theme


# 4. Bar Graph with Customized Axis and Title
ggplot(data, aes(x = category, y = values)) +
  geom_bar(stat = "identity", fill = "orange") +  # Bar plot with identity stat
  xlab("Categories") +  # Custom X-axis label
  ylab("Frequency") +  # Custom Y-axis label
  ggtitle("Customized Bar Graph") +  # Title
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold", color = "purple", size = 16),  # Center and style title
    axis.text.x = element_text(angle = 45, hjust = 1, color = "blue"),  # Rotate and color X-axis labels
    axis.text.y = element_text(color = "green")  # Color Y-axis labels
  )


# 5. Bar Graph with Stacked Bars
ggplot(data, aes(x = category, y = values, fill = group)) +
  geom_bar(stat = "identity") +  # Stacked bars by default
  xlab("Category") +  # X-axis label
  ylab("Values") +  # Y-axis label
  ggtitle("Stacked Bar Graph") +  # Title
  scale_fill_manual(values = c("X" = "skyblue", "Y" = "pink")) +  # Custom fill colors
  theme_bw()  # Black and white theme
