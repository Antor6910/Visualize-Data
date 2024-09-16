# Load ggplot2 library
library(ggplot2)

# Read the gas_price.csv
gas_data <- read.csv("gas_prices.csv")

# Sample data - replace this with your actual data
data <- data.frame(
  Year = gas_data$Year,
  Price = gas_data$Gas_Price,
  Country = gas_data$Country
)

# Create the bar graph
ggplot(data, aes(x = Year, y = Price, fill = Country)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Gas Prices over years by country", x = "Year", y = "Price") +
  theme_minimal()


