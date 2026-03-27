Z# Streak Analysis: Probability Distribution vs Empirical Data
<img width="2816" height="1536" alt="Probability Models" src="https://github.com/user-attachments/assets/cb5e5fe2-5c1c-44f4-afbc-d82134d2a275" />

## Overview
This project analyzes streak patterns in a sequence of binary outcomes (Completion vs Incompletion) using probability theory.

## Objective
- Compare empirical streak distribution with theoretical expectations
- Evaluate whether outcomes behave randomly
- Estimate expected longest streak

## Methodology
- Converted raw sequence data into streak patterns (e.g., CI, CCI, etc.)
- Built empirical distribution using pivot tables in Excel
- Calculated theoretical probabilities using:
  P(pattern) = (0.5^k) × 0.5
- Compared expected vs observed frequencies

## Key Findings
- Empirical distribution closely matches theoretical expectations
- Differences are small, indicating near-random behavior
- Expected longest run for 250 trials ≈ 8

## Tools Used
- Excel (Pivot Tables, Probability Modeling)
- Basic probability theory

## Skills Demonstrated
- Data transformation
- Probability modeling
- Pattern analysis
- Interpretation of randomness vs streakiness
