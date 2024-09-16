library(ggplot2)

# Create a sample Marriage dataset with random ages
set.seed(42)
Marriage <- data.frame(age = c(25, 30, 35, 40, 28, 32, 27, 29, 34, 33,
                               31, 38, 36, 26, 37, 45, 50, 55, 60, 22,
                               24, 39, 41, 43, 44, 23, 46, 48, 49, 52))

# Display first few rows
head(Marriage)

# Plot the smoothed density curve
ggplot(Marriage, aes(x = age)) +
  geom_density(fill = "green", color = "black", alpha = 0.6) +
  labs(title = "Density Estimate of Participants by Age", x = "Age", y = "Density")
