library(ggplot2)
library(scales)

# Create a sample Marriage dataset with random ages
set.seed(42)  # Setting seed for reproducibility
Marriage <- data.frame(age = c(25, 30, 35, 40, 28, 32, 27, 29, 34, 33,
                               31, 38, 36, 26, 37, 45, 50, 55, 60, 22,
                               24, 39, 41, 43, 44, 23, 46, 48, 49, 52))

# Display first few rows
head(Marriage)

# Plot the age distribution using a histogram
#if you want to plot the graph in y axis you can use coord_flip()
ggplot(Marriage, aes(x = age)) +
  geom_histogram(fill = "cornflowerblue", color = "white", bins = 10) +
  labs(title = "Participants by Age", x = "Age", y = "Count")+
  scale_y_continuous(labels = scales::percent_format())

