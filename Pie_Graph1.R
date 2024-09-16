# Load necessary library
library(ggplot2)

# Data for the pie chart (Subject distribution and their scores)
subjects <- c('Mathematics', 'Science', 'English', 'History', 'Art')
scores <- c(90, 80, 70, 85, 75)

# Combine the data into a data frame
data <- data.frame(
  Subject = subjects,
  Score = scores
)

# Calculate percentages for each slice
data$Percentage <- data$Score / sum(data$Score) * 100

# Create the pie chart using ggplot2
ggplot(data, aes(x = "", y = Score, fill = Subject)) +
  geom_bar(width = 1, stat = "identity") +                # Create bars with heights based on Score
  coord_polar(theta = "y") +                              # Convert bar chart to pie chart
  geom_text(aes(label = paste0(round(Percentage, 1), "%")),  # Add percentage labels
            position = position_stack(vjust = 0.5)) +     # Position labels in the middle of the slices
  labs(title = 'Distribution of Scores by Subject') +     # Title of the pie chart
  theme_void()                                            # Remove axis labels and gridlines
