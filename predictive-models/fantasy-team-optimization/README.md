# Fantasy Team Optimization & Performance Prediction

## Overview
This project applies regression analysis and optimization techniques to evaluate player performance and select the optimal fantasy team under a fixed budget. The objective is to maximize total expected points while satisfying positional and budget constraints.

This project demonstrates both **predictive analytics (regression)** and **prescriptive analytics (optimization)** in a sports analytics context.

---

## Problem Statement
Given a set of players with historical performance data:

- Predict future player performance using past season data
- Select the best combination of players to maximize total points
- Stay within a fixed budget constraint
- Ensure valid team composition (1 QB + 2 additional players)

---

## Methodology

### 1. Regression Analysis (Prediction)
- A scatter plot was created to analyze the relationship between Season 1 and Season 2 performance
- A linear regression model was fitted using the least squares method
- The regression equation was used to estimate projected player performance

**Regression Model:**
y = 0.91x + 26.43

Where:
- x = Season 1 points
- y = Predicted Season 2 points

---

### 2. Error Evaluation
- Error = Actual − Predicted
- Squared Error = (Error)²

**Results:**
- Sum of Errors (SE): ≈ 0  
- Sum of Squared Errors (SSE): 160.98  

This indicates that the model is unbiased and provides a strong fit to the data.

---

### 3. Optimization (Team Selection)

#### Manual Approach
- Evaluated all feasible player combinations using binary selection (0/1)
- Applied constraints:
  - Exactly 1 quarterback
  - Total of 3 players
  - Budget ≤ $50

**Manual Solution:**
- Team: Q2, WR1, WR2  
- Total Cost: 44  
- Total Points: 650  

---

#### Solver Approach (Optimal Solution)
- Used Excel Solver to maximize total expected points
- Decision variables: binary (0/1 player selection)
- Constraints:
  - Budget ≤ 50
  - Exactly 1 QB
  - Total players = 3

**Optimal Team:**
- QB1, RB2, WR1  
- Total Cost: 50  
- Total Points: 705  

---

## Key Insights

- The Solver method identified a more optimal solution than the manual approach by evaluating all possible combinations.
- Manual enumeration can miss optimal solutions when the decision space grows.
- Regression provides a strong foundation for predicting performance, while optimization translates predictions into actionable decisions.

---

## Tools Used
- Microsoft Excel
- Excel Solver
- Regression Analysis (Least Squares Method)

---

## Project Structure
```
│
├──fantasy-team-optimization/
│
├──README.md
│
├──excel/
│  ├──fantasy-team-optimization.xlsx
│
├──visuals
    ├──scatter_plot.png
    ├──solver_result.ong
```

---

## Files
- `excel/fantasy-team-optimization.xlsx` → Full model, calculations, and Solver setup
- `visuals/` → Supporting charts and outputs (optional)

---

## Applications
This project reflects real-world applications such as:
- Fantasy sports team selection
- Resource allocation under constraints
- Portfolio optimization
- Data-driven decision-making in consulting and analytics

---

## Note
This project was developed as part of coursework in sports analytics and demonstrates practical applications of regression modeling and optimization techniques.
