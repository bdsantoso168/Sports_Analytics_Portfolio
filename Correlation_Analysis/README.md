# Correlation Analysis

Two independent analyses exploring how statistical relationships in sports data can surface
meaningful signals, and where models built for one sport break down when applied to another.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Q1 - NBA Player Scoring Correlation](#q1---nba-player-scoring-correlation)
- [Q2 - EPL Pythagorean Win Theorem Test](#q2---epl-pythagorean-win-theorem-test)
- [How to Run](#how-to-run)
- [Dependencies](#dependencies)

---

## Project Structure

```
Correlation_Analysis/
├── README.md
├── Q1_NBA_Player_Correlation/
│   ├── NBA_Scrapper_Q1.py          # Scraper: Basketball Reference per-game stats
│   ├── NBA_2026_PerGame.csv        # Output: 614 player records, tilde-delimited
│   └── BDS_Correlation.xlsx        # Analysis: scatterplots + correlation matrix
└── Q2_EPL_Pythagorean_Win_Theorem/
    ├── EPL_Scrapper_Q2.py          # Scraper: ESPN public API standings
    └── EPL_2026_Standings.csv      # Output: 20 team records, tilde-delimited
```

---

## Q1 - NBA Player Scoring Correlation

### Overview

Player-level correlation analysis on the 2025-26 NBA season, asking which per-game
statistics are most predictive of a player's scoring output. Data was scraped from
Basketball Reference and analyzed in Excel using scatterplots and a full correlation matrix.

### Data Source

- **Source:** [Basketball Reference - NBA 2025-26 Per Game](https://www.basketball-reference.com/leagues/NBA_2026_per_game.html)
- **Scraper:** `NBA_Scrapper_Q1.py`
- **Method:** `urllib` request + `pandas.read_html` table parser
- **Output:** `NBA_2026_PerGame.csv` (614 player records, tilde `~` delimited)
- **Columns:** Player, Pos, Age, Tm, G, GS, MP, FG, FGA, FG%, 3P, 3PA, 3P%, FT, FTA,
  FT%, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS

### Data Cleaning Notes

- Multi-team players (traded mid-season) appear multiple times in the raw data. Only the
  `TOT` (combined) row is retained to avoid double-counting.
- Players with zero minutes played are excluded.
- Derived metrics (e.g., FG%) are not correlated against their own components (FG, FGA)
  to avoid definitional multicollinearity.

### Analyses Performed

**1. Single Predictor vs. Points Scored**
<img width="858" height="455" alt="Figure 1 - Free Throw Attempts vs Points Per Game - NBA 2026 Season" src="https://github.com/user-attachments/assets/682f2d84-6582-4ab0-bd77-2709fac9c3f0" />

A scatterplot and Pearson correlation were generated between field goals made (FG) and
points per game (PTS). FG showed the strongest individual association with scoring output,
which is expected given that it is the primary mechanism for accumulating points.

**2. Two Independent Variables**
<img width="860" height="419" alt="Figure 2 - Assists vs Turnovers Per Game - NBA 2026 Season" src="https://github.com/user-attachments/assets/d8fab71d-0c3a-42b6-a9f5-470f2134e679" />

A scatterplot and correlation were run between assists (AST) and turnovers (TOV) to
examine the relationship between two process-level stats. These metrics share a logical
connection since playmaking opportunity creates both assists and turnover risk. The
resulting correlation validates that higher-usage players tend to occupy both extremes of
this tradeoff.

**3. Full Correlation Matrix**

<img width="677" height="173" alt="Figure 3 - Correlation Matrix of NBA Offensive Statistics - NBA 2026 Season" src="https://github.com/user-attachments/assets/e274ea0d-75f3-40ca-91ab-7d68602fa46b" />

A complete correlation matrix was built across all scoring-relevant variables using the
Excel Data Analysis Toolpak, with conditional formatting applied to flag any pair with
r > 0.60. Key takeaways:

- **FG and PTS** produced the strongest correlation, serving as the primary predictor.
- **TRB and DRB** were flagged as highly multicollinear (r > 0.90), since total rebounds
  is the arithmetic sum of its components. Including both in a regression model would
  distort coefficients.
- **3P and FGA** showed a moderate positive correlation, reflecting that high-volume
  shooters tend to generate more attempts across all shot types.
- **STL and BLK** correlated weakly with points, confirming that defensive contributions
  operate largely independently of offensive output at the player level.

---

## Q2 - EPL Pythagorean Win Theorem Test
<img width="1072" height="361" alt="Figure 4 - EPL Pythagorean Theorem Calculation Table (all 20 teams, including Total Error = 2 636 at the bottom)" src="https://github.com/user-attachments/assets/9881cd7d-20aa-46be-a31f-d624e9335f7b" />

### Overview

Baseball's Pythagorean Win Theorem, developed by Bill James, estimates a team's expected
win percentage from its runs scored and runs allowed. It is theorized to generalize to
other sports. This analysis tests whether the formula holds for association football using
the 2025-26 English Premier League season.

The formula tested:

```
Pythagorean Win% = GF² / (GF² + GA²)
```

where GF = goals for and GA = goals against. This is algebraically equivalent to:

```
Pythagorean Win% = R² / (R² + 1),  where R = GF / GA
```

### Data Source

- **Source:** [ESPN Public API - EPL Standings](https://site.api.espn.com/apis/v2/sports/soccer/eng.1/standings)
- **Scraper:** `EPL_Scrapper_Q2.py`
- **Method:** `urllib` + `json` parsing of ESPN's public standings endpoint
- **Output:** `EPL_2026_Standings.csv` (20 teams, tilde `~` delimited)
- **Columns:** Team, MP, W, D, L, GF, GA, GD, Pts

### Calculated Metrics

For each of the 20 Premier League clubs, four values were derived:

| Metric | Formula |
|---|---|
| Scoring Ratio | GF / GA |
| Pythagorean Win% | GF² / (GF² + GA²) |
| Actual Win% | W / MP |
| Error | Pythagorean Win% - Actual Win% |

### Results

| Team | GF | GA | Pyth Win% | Actual Win% | Error |
|---|---|---|---|---|---|
| Arsenal | 62 | 24 | 0.870 | 0.656 | +0.213 |
| Manchester City | 63 | 28 | 0.835 | 0.613 | +0.222 |
| Manchester United | 56 | 43 | 0.629 | 0.484 | +0.145 |
| Aston Villa | 43 | 38 | 0.561 | 0.500 | +0.061 |
| Liverpool | 52 | 42 | 0.605 | 0.469 | +0.136 |
| Chelsea | 53 | 41 | 0.626 | 0.406 | +0.219 |
| Brentford | 48 | 44 | 0.543 | 0.406 | +0.137 |
| Everton | 39 | 37 | 0.526 | 0.406 | +0.120 |
| Brighton | 43 | 37 | 0.575 | 0.375 | +0.200 |
| Sunderland | 33 | 36 | 0.457 | 0.375 | +0.082 |
| AFC Bournemouth | 48 | 49 | 0.490 | 0.313 | +0.177 |
| Fulham | 43 | 46 | 0.466 | 0.406 | +0.060 |
| Crystal Palace | 35 | 36 | 0.486 | 0.355 | +0.131 |
| Newcastle United | 45 | 47 | 0.478 | 0.375 | +0.103 |
| Leeds United | 37 | 48 | 0.373 | 0.226 | +0.147 |
| Nottingham Forest | 32 | 44 | 0.346 | 0.250 | +0.096 |
| West Ham United | 40 | 57 | 0.330 | 0.250 | +0.080 |
| Tottenham Hotspur | 40 | 51 | 0.381 | 0.219 | +0.162 |
| Burnley | 33 | 63 | 0.215 | 0.125 | +0.090 |
| Wolverhampton | 24 | 58 | 0.146 | 0.094 | +0.052 |

**Aggregate Error Summary:**
- Total Error: +2.636
- Mean Absolute Error: 0.132 (~13 percentage points per team)
- Largest overestimate: Manchester City (+0.222)
- Smallest overestimate: Wolverhampton Wanderers (+0.052)

### Conclusion

**The Baseball Pythagorean Theorem does not translate effectively to soccer.**

The model overestimated win percentage for every single team in the league, with a mean
absolute error of approximately 13 percentage points. This is a systematic bias, not
random noise, which points to a structural mismatch between the formula's assumptions and
how soccer outcomes are distributed.

The core issue is that baseball is a binary outcome sport: every game produces exactly one
winner and one loser. The Pythagorean formula is calibrated to that structure. Soccer
introduces a third outcome, the draw, which has no equivalent in baseball. Across the 2025-26
EPL season, draws accounted for a meaningful share of all results. When a team plays to a
0-0 or 1-1 draw, it earns a point but registers zero wins. The formula treats the goal
differential from that match as evidence of winning capacity, then maps it back to a
win percentage scale that does not account for the draw credit the team actually received.

The result is a model that reads a team's goal ratio as stronger than their win column
reflects, inflating predictions across the board. Adjusting the exponent or incorporating
draw rate as a correction factor would be necessary steps before applying any
Pythagorean-style model to football data.

---

## How to Run

**Q1 - NBA Scraper:**

```bash
python3 NBA_Scrapper_Q1.py
# Output: NBA_2026_PerGame.csv
```

**Q2 - EPL Scraper:**

```bash
python3 EPL_Scrapper_Q2.py
# Output: EPL_2026_Standings.csv
```

Both CSVs are tilde `~` delimited. To import into Excel, use Power Query and set the
delimiter to `~`.

---

## Dependencies

```
pandas
urllib (standard library)
json (standard library)
```

Install:

```bash
pip install pandas
```
