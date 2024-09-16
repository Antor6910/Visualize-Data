#ggplot2 uses a grammar of graphics which means creating plots involves
#mapping data to visual elements(likke points or lines) .

#Basic structure:A ggplot2 plot consists of:
  #Data:the dataset being plotted.
  #Aesthetics(aes):Mapping of variables to visual propertise(e.g->x,y,color)
  #Geomatries(geoms):Visual elements that represent data points(e.g,points,line,bars)

#ggplot documentation;

#load necessary liabrary
library(ggplot2)
#Examples dataset:'mtcars'
data(matcars)

#scatter plot of 'mpg' vs 'wt'
ggplot(data=matcars,mapping = aes(x=wt,y=mpg))+geom_point()


#Adding layers and Geoms
   #geom_points():creates a scatter plot
   #geom_line():creates a line plot
   #geom_bar():creates a bar plot
   #geom_histogram():creates histogram
   #geom_boxplot():creates a box plot
   #geom_smooth():creates scatter plot

# Scatter plot with a linear trend line (geom_smooth)
ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", col = "red",size=3)

# Map color to 'cyl' (number of cylinders)
ggplot(data = mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point(size = 3)

#Faceting allows you to create multiple plots based on the values of a categorical variable
   #facet_wrap():Facets by a single variable
   #facet_grid():Facets by two variables

# Facet by 'cyl' using facet_wrap
ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  facet_wrap(~ cyl)

#Adding titles and labels
    #labs():Add labels and titles
    #xlab() and ylab():Add labels for the x and y axis
    #ggtitle():Adds a main title to the plot
# Add titles and labels
ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  labs(title = "Scatter Plot of MPG vs Weight", x = "Weight", y = "Miles per Gallon")

/* Modifying Scales
*scale_x_continuous() and scale_y_continuous(): Modify the scales of the x and y axes.
*scale_color_manual(): Customizes colors.
*scale_fill_gradient(): For continuous color scales.

*/
# Customize color scale
ggplot(data = mtcars, aes(x = wt, y = mpg, color = mpg)) +
  geom_point(size = 3) +
  scale_color_gradient(low = "blue", high = "red")

#Coordinate Systems
#    coord_flip(): Flips the x and y axes.
#    coord_polar(): Creates polar coordinates (for pie charts, etc.).

# Bar plot with flipped coordinates
ggplot(data = mtcars, aes(x = factor(cyl), fill = factor(cyl))) +
  geom_bar() +
  coord_flip()

/*
Position Adjustments
position = "dodge": Separates bars.
position = "fill": Creates a stacked percentage bar chart.
*/
# Stacked bar plot with dodge position
ggplot(data = mtcars, aes(x = factor(cyl), fill = factor(gear))) +
  geom_bar(position = "dodge")

/*
  Saving Plots
ggsave(): Saves the last plot to a file.
*/
# Save plot to a file
p <- ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point()

ggsave("scatter_plot.png", plot = p, width = 8, height = 6)


/*
Advanced Features
Annotations: Adding text or shapes to plots.
Custom Geometries: Creating custom plots by defining new geoms.
Interactive Plots: Using plotly with ggplot2 for interactive visualizations.
*/
# Add a text annotation
ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  annotate("text", x = 5, y = 30, label = "Outlier", color = "red", size = 5)

/*
Combining Multiple Plots
patchwork, gridExtra, or cowplot: Combine multiple ggplot2 plots into a single plot.
*/
library(patchwork)

p1 <- ggplot(data = mtcars, aes(x = wt, y = mpg)) + geom_point()
p2 <- ggplot(data = mtcars, aes(x = factor(cyl), fill = factor(cyl))) + geom_bar()

# Combine using patchwork
p1 + p2


