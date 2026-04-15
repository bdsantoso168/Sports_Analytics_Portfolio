#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:52:29 2026

@author: benedictsantoso
"""

import urllib.request
import pandas as pd
import io

# -------------------------------------------------------
# ISOM 232 - Correlation Assignment
# Q1: NBA 2025-26 Per Game Player Stats
# Source: basketball-reference.com
# Output: NBA_2026_PerGame.csv  (tilde delimited, ASCII)
# -------------------------------------------------------

url = "https://www.basketball-reference.com/leagues/NBA_2026_per_game.html"
output_file = "NBA_2026_PerGame.csv"

print("Fetching NBA 2025-26 per game stats...")

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
)

response = urllib.request.urlopen(req)
html = response.read().decode("utf-8", errors="replace")

# pandas read_html is much more reliable for basketball-reference tables
tables = pd.read_html(io.StringIO(html))

if not tables:
    print("ERROR: No tables found on the page.")
    exit()

# basketball-reference per_game page — grab the largest table
df = max(tables, key=lambda t: len(t))

print(f"Raw table shape: {df.shape}")

# Flatten multi-index columns if present
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [str(c[1]) if c[1] else str(c[0]) for c in df.columns]
else:
    df.columns = [str(c) for c in df.columns]

print(f"Columns found: {list(df.columns)}")

# Remove repeated header rows basketball-reference inserts every 20 rows
if "Player" in df.columns:
    df = df[df["Player"] != "Player"]

# Drop rank column if present
if "Rk" in df.columns:
    df = df.drop(columns=["Rk"])

# Normalize team column name (basketball-reference sometimes uses "Team" instead of "Tm")
if "Team" in df.columns and "Tm" not in df.columns:
    df = df.rename(columns={"Team": "Tm"})

# Keep only the columns we need
wanted_cols = [
    "Player", "Pos", "Age", "Tm", "G", "GS", "MP",
    "FG", "FGA", "FG%",
    "3P", "3PA", "3P%",
    "FT", "FTA", "FT%",
    "ORB", "DRB", "TRB",
    "AST", "STL", "BLK", "TOV", "PF", "PTS"
]

# Only keep columns that actually exist in scraped data
existing_cols = [c for c in wanted_cols if c in df.columns]
print(f"Columns being used: {existing_cols}")
df = df[existing_cols]

# Convert numeric columns
numeric_cols = [c for c in existing_cols if c not in ["Player", "Pos", "Tm"]]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# For traded players, keep only the TOT (totals) row
if "Tm" in df.columns:
    multi_team = df[df["Tm"] == "TOT"]["Player"].unique()
    df = df[~((df["Player"].isin(multi_team)) & (df["Tm"] != "TOT"))]

# Filter out players with fewer than 10 games
if "G" in df.columns:
    df = df[df["G"] >= 10]

# Drop rows missing player name or points
df = df.dropna(subset=["Player", "PTS"])
df = df.reset_index(drop=True)

print(f"Players after cleaning: {len(df)}")
print(f"\nSample data:")
print(df[["Player", "Tm", "G", "PTS", "AST", "TRB", "FG%"]].head(10).to_string(index=False))

# Write tilde-delimited ASCII CSV
df.to_csv(
    output_file,
    sep="~",
    index=False,
    encoding="ascii",
    errors="replace"
)

print(f"\nDone! File saved: {output_file}")
print(f"Total players: {len(df)}")
print("Import into Excel via Power Query and set delimiter to tilde (~)")