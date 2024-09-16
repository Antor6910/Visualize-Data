# Open a new graphics window
x11()

# Basic Scatter Plot with Lines in R
x <- c(1, 2, 3, 4, 5)  # X-axis values
y <- c(2, 4, 3, 6, 7)  # Y-axis values

# Plotting the Graph
plot(x, y, type = "b", col = "blue",   # type = "b" for both points and lines
     main = "Scatter Plot with Lines", # Title of the graph
     xlab = "X Values",                # X-axis label
     ylab = "Y Values")                # Y-axis label

# Adding a Grid
grid()
