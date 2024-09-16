# Load necessary library
library(ggplot2)

# Data for the bar graph (Student names and their scores in three subjects)
students <- c('Alice', 'Bob', 'Charlie', 'David', 'Eve')
subject1 <- c(85, 92, 78, 90, 88)
subject2 <- c(75, 82, 88, 85, 80)
subject3 <- c(95, 89, 84, 80, 90)

# Combine the subject scores into a data frame
data <- data.frame(
  Student = rep(students, times = 3),  # Repeat student names for each subject
  Subject = factor(rep(c('Subject 1', 'Subject 2', 'Subject 3'), each = length(students))),  # Repeat subject names for each student
  Score = c(subject1, subject2, subject3)  # Combine all subject scores into a single vector
)

# Create the stacked bar graph
ggplot(data, aes(x = Student, y = Score, fill = Subject)) +
  geom_bar(stat = "identity") +                # Create bars with heights based on Score
  scale_fill_manual(values = c('red', 'blue', 'green')) +  # Manually set colors for each subject
  labs(title = 'Scores of Different Students by Subject',    # Title of the bar graph
       x = 'Students',                                  # Label for the x-axis
       y = 'Scores',                                    # Label for the y-axis
       fill = 'Subjects')                              # Label for the legend
