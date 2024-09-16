# Load necessary library
library(ggplot2)

# Create a sample data frame
data <- data.frame(
  Category = c("A", "B", "C", "D"),
  Value = c(10, 20, 30, 40),
  Group = c("X", "Y", "X", "Y")  # Additional variable for coloring
)

# Bar Graph with Different Colors
ggplot(data, aes(x = Category, y = Value, fill = Group)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(title = "Bar Graph with Different Colors", x = "Category", y = "Value") +
  scale_fill_brewer(palette = "Set3")  # Choose a color palette

