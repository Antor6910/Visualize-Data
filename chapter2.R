# Load necessary libraries
library(dplyr)
library(tidyr)

#The starwars dataset is a built-in dataset in the dplyr package in R.
# It contains information about characters from the Star Wars franchise

# Sample data: starwars dataset from dplyr
data(starwars)

# 1. Keep the variables name, height, and gender
newdata <- select(starwars, name, height, gender)
print(newdata)

# 2. Keep the variables name and all variables between mass and species inclusive
newdata <- select(starwars, name, mass:species)
print(newdata)

# 3. Keep all variables except birth_year and gender
newdata <- select(starwars, -birth_year, -gender)
print(newdata)

# 4. Select females
newdata <- filter(starwars, gender == "female")
print(newdata)

# 5. Select females that are from Alderaan
newdata <- filter(starwars, gender == "female" & homeworld == "Alderaan")
print(newdata)

# 6. Select individuals that are from Alderaan, Coruscant, or Endor
newdata <- filter(starwars, homeworld %in% c("Alderaan", "Coruscant", "Endor"))
print(newdata)

# 7. Convert height in centimeters to inches and mass in kilograms to pounds
newdata <- mutate(starwars,
                  height = height * 0.394,
                  mass = mass * 2.205)
print(newdata)

# 8. Create a new variable 'heightcat' based on height
newdata <- mutate(starwars, heightcat = ifelse(height > 180, "tall", "short"))
print(newdata)

# 9. Convert any eye color that is not black, blue, or brown to "other"
newdata <- mutate(starwars,
                  eye_color = ifelse(eye_color %in% c("black", "blue", "brown"), eye_color, "other"))
print(newdata)

# 10. Set heights greater than 200 or less than 75 to missing
newdata <- mutate(starwars, height = ifelse(height < 75 | height > 200, NA, height))
print(newdata)

# 11. Calculate mean height and mass
mean_stats <- summarize(starwars,
                        mean_ht = mean(height, na.rm = TRUE),
                        mean_mass = mean(mass, na.rm = TRUE))
print(mean_stats)

# 12. Calculate the mean height and weight by gender
newdata <- starwars %>%
  group_by(gender) %>%
  summarize(mean_ht = mean(height, na.rm = TRUE),
            mean_wt = mean(mass, na.rm = TRUE))
print(newdata)

# 13. Calculate the mean height by species for females
newdata <- starwars %>%
  filter(gender == "female") %>%
  group_by(species) %>%
  summarize(mean_ht = mean(height, na.rm = TRUE))
print(newdata)

# 14. Reshaping data: Convert wide dataset to long dataset
wide_data <- starwars %>%
  select(name, height, mass) # example data
longdata <- pivot_longer(wide_data, cols = c("height", "mass"),
                         names_to = "variable",
                         values_to = "value")
print(longdata)

# 15. Convert long dataset to wide dataset
wide_data <- pivot_wider(longdata,
                         names_from = "variable",
                         values_from = "value")
print(wide_data)


