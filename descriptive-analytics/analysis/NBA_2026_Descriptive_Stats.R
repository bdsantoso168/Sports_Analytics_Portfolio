# Load Data
NBA_ST <- read.csv("NBA_2026_PerGame.csv")

# Check Structure
dim(NBA_ST)
names(NBA_ST)

# Descriptive Statistics for PTS
mean(NBA_ST$PTS, na.rm=TRUE)
median(NBA_ST$PTS, na.rm=TRUE)
sd(NBA_ST$PTS, na.rm=TRUE)
var(NBA_ST$PTS, na.rm=TRUE)
min(NBA_ST$PTS, na.rm=TRUE)
max(NBA_ST$PTS, na.rm=TRUE)

hist(NBA_ST$PTS,
+      breaks = 20,
+      main = "Histogram of Points Per Game (NBA 2026)",
+      xlab = "Points Per Game",
+      col = "lightblue",
+      border = "black")

# Five Number Summary
summary(NBA_ST$PTS)

# Boxplot
boxplot(NBA_ST$PTS,
        main="Boxplot of Points Per Game (NBA 2026)",
        ylab="Points Per Game",
        col="lightgreen")