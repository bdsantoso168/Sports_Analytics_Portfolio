# Regression Analysis

ISOM 232 Sports Analytics in Action | Suffolk University | Spring 2026

This folder contains a regression analysis assignment exploring how well statistical performance metrics predict outcomes in the NFL and NBA using R.

---

## Assignment Overview

Two regression models were built using real sports data to analyze the relationship between performance metrics and team/player outcomes.

---

## Part 1 NFL Simple Linear Regression

**Question:** Does total yardage predict how many points an NFL team scores?

- **Dependent variable:** Points per Game
- **Independent variable:** Yards per Game
- **Method:** Simple linear regression in R

**Key Finding:** A statistically significant positive relationship was found between yards gained and points scored, confirming that offensive efficiency is a strong predictor of scoring output in the NFL.

---

## Part 2 NBA Salary Prediction (Multiple Regression)

**Question:** Which on-court stats best predict an NBA player's salary?

Two models were compared:

| Model | Predictors | Focus |
|---|---|---|
| Model 1 (Offensive) | Points, Assists, FG Made, FG% | Offensive production |
| Model 2 (Defensive) | Blocks, Steals, Defensive Rebounds | Defensive contribution |

**Key Finding:** Offensive statistics explained a significantly larger share of salary variance than defensive stats, suggesting the NBA market rewards scoring and playmaking more than defense.

---

## Tools Used

- **R / RStudio** for regression modeling and visualization
- **Excel** for initial data inspection

---

## Folder Structure

```
regression-analysis/
├── README.md
├── scripts/
│   └── ISOM232_Regression_NFL_NBA.R
├── data/
│   ├── NationalFootballLeague.xlsx
│   └── NBA.xlsx
└── visuals/
    ├── nfl_scatter_plot.png
    ├── nfl_regression_summary.png
    ├── nba_offensive_model_summary.png
    └── nba_defensive_model_summary.png
```

---

## Data Sources

- NFL team statistics sourced from in-class dataset (Suffolk University ISOM 232)
- NBA player statistics sourced from in-class dataset (Suffolk University ISOM 232)
