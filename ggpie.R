library(ggpie)
# Create a sample dataset
data <- data.frame(
  category = c("A", "B", "C", "D"),
  value = c(30, 15, 45, 10)
)

# Create the pie chart using ggpie
ggpie(data,
      labels = data$category,
      fill = "category",
      color = "white",
      palette = "Set3",
      title = "Pie Chart of Categories",
      label = paste0(data$category, ": ", data$value, "%"))
/*
label: Specifies the text labels for each slice.
fill: Defines the fill color for the pie slices based on the category.
color: The color of the borders of the pie slices.
palette: Defines the color palette for the slices.
title: Adds a title to the pie chart.
*/