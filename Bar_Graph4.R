# Data for the bar graph (students and their scores)
students <- c('John', 'Mary', 'Alex', 'Sara', 'David')
scores <- c(85, 90, 78, 88, 95)

# List of colors for each bar (one color per student)
colors <- c('skyblue', 'orange', 'green', 'purple', 'red')

# Create the bar graph
barplot(scores,
        names.arg = students,
        col = colors,
        main = 'Students and Their Scores',
        xlab = 'Students',
        ylab = 'Scores',
        ylim = c(0, 100))  # Setting y-axis limit for scores out of 100

# Display the plot
