# Load necessary libraries
library(ggplot2)
library(reshape2)

# Read the data from the CSV file
gas_data <- read.csv("gas_prices.csv")

# Check the column names to ensure correct references
colnames(gas_data)

# Correctly reference columns without spaces
# Example: "South.Korea" instead of "South Korea"
selected_countries <- gas_data[, c("Year", "USA", "South.Korea", "Canada", "Australia", "UK")]

# Remove any rows with missing values
selected_countries <- na.omit(selected_countries)

# Reshape data for ggplot2 (from wide to long format)
data_long <- melt(selected_countries, id.vars = "Year",
                  variable.name = "Country", value.name = "Gas_Price")

# Plot the line graph with a minimum 2-year interval on the x-axis
ggplot(data_long, aes(x = Year, y = Gas_Price, color = Country)) +
  geom_line(size = 1) +
  labs(title = "Gas Prices Over Years", x = "Year", y = "Gas Price (USD)") +
  scale_x_continuous(breaks = seq(min(selected_countries$Year), max(selected_countries$Year), by = 2)) +
  theme_minimal()


