## Par 1 - Simple Linear Regression

# Install readxl if you haven't already
install.packages("readxl")
library(readxl)

# Load the NFL data
nflData <- read_excel("/Users/benedictsantoso/Documents/Sports Analytics (ISOM 232) - LOCAL/NationalFootballLeague.xlsx", skip = 2)

# Check the first few rows and column names
head(nflData)

# Turn off scientific notation
options(scipen = 9999)

# Scatter plot
plot(nflData$`Yards/Game`, nflData$`Points/Game`,
     main = "NFL: Yards/Game vs Points/Game",
     xlab = "Yards/Game",
     ylab = "Points/Game",
     pch = 19, col = "steelblue")

# Add regression trend line
abline(lm(nflData$`Points/Game` ~ nflData$`Yards/Game`), col = "red", lwd = 2)

# Build regression model
nflModel <- lm(nflData$`Points/Game` ~ nflData$`Yards/Game`)

# View model details
summary(nflModel)

## Part 2 - NBA Salary Prediction Models
# Load NBA data
nbaData <- read_excel("/Users/benedictsantoso/Documents/Sports Analytics (ISOM 232) - LOCAL/NBA.xlsx")

# Filter to regular season only and remove missing salaries
nbaData <- nbaData[nbaData$Postseason == FALSE, ]
nbaData <- nbaData[!is.na(nbaData$Salary), ]

# Verify
head(nbaData)

# Turn off scientific notation
options(scipen = 9999)

# MODEL 1 - Offensive stats predicting Salary
nbaOffensive <- lm(Salary ~ Points + Assists + FG_made + FG_percent, data = nbaData)
summary(nbaOffensive)

# MODEL 2 - Defensive stats predicting Salary
nbaDefensive <- lm(Salary ~ Blocks + Steals + Rebound_def, data = nbaData)
summary(nbaDefensive)