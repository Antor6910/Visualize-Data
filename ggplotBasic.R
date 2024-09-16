# Load necessary library
library(ggplot2)
library(patchwork)  # For combining plots

# Use the built-in mtcars dataset
data("mtcars")

# 1. Scatter Plot of 'mpg' (miles per gallon) vs 'wt' (weight)
ggplot(data = mtcars, mapping = aes(x = wt, y = mpg)) +
  geom_point() +
  labs(title = "Scatter Plot of MPG vs Weight", x = "Weight (1000 lbs)", y = "Miles per Gallon (MPG)")

# 2. Scatter Plot with a Linear Trend Line (geom_smooth)
ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", col = "red", size = 1.5) +
  labs(title = "Scatter Plot with Linear Trend Line", x = "Weight (1000 lbs)", y = "Miles per Gallon (MPG)")

# 3. Map Color to 'cyl' (number of cylinders)
ggplot(data = mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point(size = 3) +
  labs(title = "Scatter Plot Colored by Number of Cylinders", x = "Weight (1000 lbs)", y = "Miles per Gallon (MPG)", color = "Cylinders")

# 4. Facet by 'cyl' using facet_wrap
ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  facet_wrap(~ cyl) +
  labs(title = "Scatter Plot Faceted by Number of Cylinders", x = "Weight (1000 lbs)", y = "Miles per Gallon (MPG)")

# 5. Customize Color Scale using scale_color_gradient
ggplot(data = mtcars, aes(x = wt, y = mpg, color = mpg)) +
  geom_point(size = 3) +
  scale_color_gradient(low = "blue", high = "red") +
  labs(title = "Scatter Plot with MPG Color Gradient", x = "Weight (1000 lbs)", y = "Miles per Gallon (MPG)")

# 6. Bar Plot with Flipped Coordinates (coord_flip)
ggplot(data = mtcars, aes(x = factor(cyl), fill = factor(cyl))) +
  geom_bar() +
  coord_flip() +
  labs(title = "Bar Plot of Cylinders with Flipped Coordinates", x = "Cylinders", y = "Count", fill = "Cylinders")

# 7. Stacked Bar Plot with Dodge Position
ggplot(data = mtcars, aes(x = factor(cyl), fill = factor(gear))) +
  geom_bar(position = "dodge") +
  labs(title = "Stacked Bar Plot of Cylinders by Gear", x = "Cylinders", y = "Count", fill = "Gear")

# 8. Add a Text Annotation
ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  annotate("text", x = 5, y = 30, label = "Outlier", color = "red", size = 5) +
  labs(title = "Scatter Plot with Annotation", x = "Weight (1000 lbs)", y = "Miles per Gallon (MPG)")

# 9. Saving a Plot to a File
p <- ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  labs(title = "Scatter Plot of MPG vs Weight", x = "Weight (1000 lbs)", y = "Miles per Gallon (MPG)")

ggsave("scatter_plot.png", plot = p, width = 8, height = 6)

# 10. Combining Multiple Plots using patchwork
p1 <- ggplot(data = mtcars, aes(x = wt, y = mpg)) + geom_point() +
  labs(title = "Scatter Plot of MPG vs Weight", x = "Weight", y = "MPG")

p2 <- ggplot(data = mtcars, aes(x = factor(cyl), fill = factor(cyl))) + geom_bar() +
  labs(title = "Bar Plot of Cylinders", x = "Cylinders", y = "Count", fill = "Cylinders")

# Combine plots using patchwork
combined_plot <- p1 + p2
print(combined_plot)
