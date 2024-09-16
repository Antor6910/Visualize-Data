# Data for the bar graph (Student names and their scores in three subjects)
students <- c('Alice', 'Bob', 'Charlie', 'David', 'Eve')  # Vector of student names
subject1 <- c(85, 92, 78, 90, 88)  # Scores for Subject 1
subject2 <- c(75, 82, 88, 85, 80)  # Scores for Subject 2
subject3 <- c(95, 89, 84, 80, 90)  # Scores for Subject 3

# Combine the subject scores into a matrix
scores_matrix <- rbind(subject1, subject2, subject3)  # Each row represents a subject, and each column represents a student

# List of colors for each subject
colors <- c('red', 'blue', 'green')  # Colors for the bars corresponding to each subject

# Create the stacked bar graph
barplot(scores_matrix,                   # The matrix of scores to plot
        beside = FALSE,                  # Create a stacked bar graph (FALSE means stacked)
        col = colors,                    # Colors for each subject
        legend.text = c('Subject 1', 'Subject 2', 'Subject 3'),  # Labels for the legend
        args.legend = list(title = "Subjects"),  # Title for the legend
        main = 'Scores of Different Students by Subject',  # Title of the bar graph
        xlab = 'Students',                # Label for the x-axis
        ylab = 'Scores',                  # Label for the y-axis
        names.arg = students)             # Labels for the x-axis (student names)

# Display the plot
