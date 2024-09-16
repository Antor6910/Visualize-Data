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

# Create the pie chart using ggplot2
ggplot(data, aes(x = "", y = Score, fill = Subject)) +
  geom_bar(width = 1, stat = "identity") +  # Create bars with heights based on Score
  coord_polar(theta = "y") +                 # Convert bar chart to pie chart
  labs(title = 'Distribution of Scores by Subject') +  # Title of the pie chart
  theme_void()  # Remove axis labels and gridlines
