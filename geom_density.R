library(ggplot2)


# Create a new dataset with different sample data
set.seed(123)  # Set seed for reproducibility
New_Marriage <- data.frame(age = c(20, 12, 18, 10, 25, 50, 10, 7, 14, 35,
                                   28, 10, 35, 20, 25, 58, 60, 30, 65, 28,
                                   60, 75, 13, 78, 80, 82, 85, 88, 90, 92))

# Save the new dataset to a CSV file
write.csv(New_Marriage, file = "New_Marriage_data.csv", row.names = FALSE)

# Read the new dataset from the CSV file
New_Marriage <- read.csv("New_Marriage_data.csv")

# Calculate the bandwidth using bw.nrd()
bandwidth <- bw.nrd(New_Marriage$age)

# Plot the smoothed density curve with custom bandwidth
ggplot(New_Marriage, aes(x = age)) +
  geom_density(bw = bandwidth, fill = "skyblue", color = "black", alpha = 0.6) +
  labs(title = "Density Estimate of Participants by Age", x = "Age", y = "Density")
