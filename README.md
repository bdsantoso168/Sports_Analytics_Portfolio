# Sports Outcome Prediction Using Solver Optimization
![SuperBowel and NBA Predictor Thumbnail.png…]()

This repository contains an **educational sports analytics project** that applies **Excel Solver–based optimization** to model and compare game outcomes across multiple professional sports leagues. The project demonstrates how least-squares optimization can be used to estimate **relative team strength** and **home advantage**, and how model behavior varies across sports with different scoring structures.

> ⚠️ **Note**  
> This project was completed as part of an academic course and follows instructional methodology. It is intended for **learning and portfolio demonstration purposes only**.

---

## Project Overview

The goal of this project is to explore how **optimization techniques** can be applied to real-world sports data to:

- Estimate team ratings based on historical game results  
- Quantify home-field / home-court advantage  
- Compare model behavior across different sports environments  

Two leagues are analyzed:
- **NFL** – Low-scoring, high-variance environment
  ![NFL Solver Summary](assets/screenshots/NFL_solver_summary.png)
- **NBA** – High-scoring, large-sample environment
  ![NBA Solver Summary](assets/screenshots/NBA_solver_summary.png)

Both models use the same underlying framework but produce different numerical characteristics due to sport-specific dynamics.

---

### Example Neutral-Site Team Comparison (Super Bowl)

The following comparison illustrates how the optimized team ratings translate into a predicted point margin under a neutral-site assumption (no home-field advantage applied).

![NFL Super Bowl Team Comparison](assets/screenshots/NFL_superbowl_prediction.png)

### Example Neutral-Site Team Comparison

This example compares two NBA teams using optimized ratings to demonstrate how relative team strength translates into an expected point margin under neutral-site conditions.

![NBA Celtics vs Lakers Comparison](assets/screenshots/NBA_celtics_lakers_comparison.png)

---

## End-to-End Workflow

This project follows a structured analytics pipeline:

1. **Data Scraping (Python)**
   - Python scripts were used to scrape historical game results from publicly available sports reference websites.
   - Game-level data was exported into CSV format for downstream analysis.

2. **Data Preparation (Excel Power Query)**
   - CSV files were imported into Excel using Power Query.
   - Data was cleaned, standardized, and transformed into a consistent game-level structure.
   - Home teams, away teams, scores, and margins were prepared for modeling.

3. **Modeling & Optimization (Excel Solver)**
   - A least-squares optimization model was constructed in Excel.
   - Solver was used to minimize the sum of squared errors (SSE) between actual and predicted margins.
   - Team ratings and a home advantage parameter were optimized, subject to an average-rating constraint.

4. **Interpretation & Comparison**
   - Neutral-site comparisons were used to interpret team ratings.
   - Model behavior was compared across the NFL and NBA to highlight sport-specific dynamics.

---

## Modeling Approach

For each league, the following steps were performed:

1. **Data Collection**
   - Game results were scraped from publicly available sports reference websites using Python.
2. **Data Preparation**
   - Data was cleaned and structured using Excel Power Query.
   - Game-level margins were computed.
3. **Solver Optimization**
   - Excel Solver was used to minimize the **sum of squared errors (SSE)** between actual and predicted margins.
   - Team ratings and a home advantage parameter were optimized.
   - A constraint was imposed such that the **average team rating equals zero**.
4. **Interpretation**
   - Model outputs were analyzed and compared across sports.
   - Neutral-site comparisons were used to illustrate how ratings translate into predicted margins.

---

## NFL Model (Super Bowl Application)

- Based on 2025 NFL regular season data
- Includes estimation of home-field advantage
- Super Bowl treated as a **neutral-site game**
- Final output includes a predicted point margin between the two Super Bowl teams

**Key takeaway:**  
NFL outcomes exhibit higher relative volatility due to fewer games and lower scoring, resulting in larger sensitivity to individual matchups.

---

## NBA Model (Cross-Sport Extension)

- Based on 2026 NBA regular season data
- Uses the same Solver framework as the NFL model
- Produces a tighter distribution of team ratings and a smaller home-court advantage

An example neutral-site comparison (Boston Celtics vs. Los Angeles Lakers) is included to demonstrate how NBA ratings can be interpreted.

**Key takeaway:**  
Higher scoring and larger sample sizes in the NBA lead to more stable optimization behavior compared to the NFL.

---

## Repository Structure

---

## Repository Structure

```text
sports-outcome-prediction-solver/
├── README.md
├── docs/
│   └── SuperBowl_and_Multi_Sport_Outcome_Prediction.pdf
├── models/
│   ├── NFL/
│   │   └── NFL2025SBResults.xlsx
│   └── NBA/
│       └── NBA2026SBResults.xlsx
├── data/
│   ├── NFL/
│   │   └── NFL2025ResultsPrepped.xlsx
│   └── NBA/
│       └── NBA2026ResultsPrepped.xlsx
├── scripts/
│   ├── nfl_scraper.py
│   └── nba_scraper.py
└── assets/
    └── screenshots/
```
---

## Tools & Technologies

- **Microsoft Excel**
  - Solver (GRG Nonlinear)
  - Power Query
- **Python**
  - Data scraping
  - CSV generation
- **GitHub**
  - Project documentation and version control

---

## How to Explore the Models

1. Open the Excel files in the `models/` folder.
2. Ensure the **Solver Add-in** is enabled in Excel.
3. Review:
   - Team ratings
   - Home advantage parameter
   - SSE objective
   - Neutral-site comparison blocks

No code execution is required to view results.

---

## Disclaimer

This repository represents an **academic coursework project** completed for instructional purposes.  
All data sources are publicly available, and all modeling follows classroom methodology.  
The results are **not intended for real-world forecasting, betting, or commercial use**.

---

## Author

**Benedict Daxell Santoso**  
Business Analytics & Information Systems  
Portfolio: GitHub projects focused on analytics, optimization, and data-driven decision-making
