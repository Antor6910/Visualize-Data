
# Open a new graphics window
x11()
# Data for the Bar Graph
fruits <- c("Apple", "Banana", "Cherry", "Date", "Elderberry")  # Categories
counts <- c(10, 15, 7, 12, 5)  # Corresponding counts for each category

# Creating a Bar Graph
barplot(counts,
        names.arg = fruits,          # Labels for the bars
        col = "skyblue",             # Color of the bars
        main = "Fruit Count Bar Graph",  # Main title
        xlab = "Fruits",             # X-axis label
        ylab = "Count",              # Y-axis label
        border = "black")            # Color of the bar borders

# Adding Gridlines
grid(nx = NA, ny = NULL)  # Adds horizontal gridlines for clarity
6