# Descriptive Statistical Analysis

## Project Objective

This project conducts a descriptive statistical analysis of NBA 2026 per-game player performance metrics using Excel and R.  

The goal is to examine distribution patterns, variability, and potential outliers in key performance variables.

---

## Variables Analyzed

- **PTS** – Points Per Game  
- **MP** – Minutes Played Per Game  
- **TRB** – Total Rebounds Per Game  

---

## Methodology

### 1. Data Source
NBA 2026 Per Game statistics from Basketball Reference.

### 2. Excel Analysis
- Descriptive Statistics (Mean, Median, Standard Deviation, Variance)
- Range and Interquartile Range (IQR)
- Manual validation of key metrics
- Outlier detection using the 1.5 × IQR rule

### 3. R Statistical Analysis
- Histogram visualization
- Boxplot visualization
- Summary statistics verification

---

## Key Statistical Measures

For each variable (PTS, MP, TRB), the following were computed:

- Mean  
- Median  
- Standard Deviation  
- Variance  
- Minimum  
- Maximum  
- IQR  
- Outlier thresholds  

---

## Visualization Outputs

R-generated visualizations are stored in the `visuals/` folder:

- Histograms for distribution shape analysis  
- Boxplots for variability and outlier detection  

---

## Observations

- **PTS** distribution exhibits right-skewness due to high-scoring players.
- **MP** distribution approximates a more normal structure.
- **TRB** shows moderate variability with limited extreme outliers.
- No extreme outliers detected under the 1.5×IQR rule.

---

## Tools Used

- Microsoft Excel (Descriptive Statistics ToolPak)
- R (Base statistical functions and visualization)
- Data cleaning and validation techniques

---

## Repository Structure

```text
descriptive-analytics/
│
├── README.md
│
├── data/
│   └── NBA_2026_PerGame.csv
│
├── analysis/
│   ├── nba_2026_descriptive_statistics.xlsx
│   └── nba_2026_descriptive_analysis.R
│
└── visuals/
    ├── pts_histogram.png
    ├── pts_boxplot.png
    ├── mp_histogram.png
    ├── mp_boxplot.png
    ├── trb_histogram.png
    └── trb_boxplot.png
```
---

## Analytical Focus

This project emphasizes statistical foundations prior to predictive modeling, reinforcing core principles in:

- Distribution analysis  
- Variability measurement  
- Outlier detection  
- Statistical validation  
