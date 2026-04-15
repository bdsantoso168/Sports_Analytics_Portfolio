#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:54:03 2026

@author: benedictsantoso
"""

import urllib.request
import json
import pandas as pd

# -------------------------------------------------------
# ISOM 232 - Correlation Assignment
# Q2: EPL 2025-26 Team Standings
# Source: ESPN public API
# Output: EPL_2026_Standings.csv  (tilde delimited, ASCII)
# -------------------------------------------------------

url = "https://site.api.espn.com/apis/v2/sports/soccer/eng.1/standings"
output_file = "EPL_2026_Standings.csv"

print("Fetching EPL 2025-26 standings from ESPN API...")

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
)

try:
    response = urllib.request.urlopen(req)
    raw = response.read().decode("utf-8")
    data = json.loads(raw)
except Exception as e:
    print(f"ERROR: {e}")
    import sys; sys.exit()

# Debug: print ALL stat keys and values for first team so we can see exact names
first_entry = data["children"][0]["standings"]["entries"][0]
print("\nDEBUG - All stats for", first_entry["team"]["displayName"])
for s in first_entry["stats"]:
    print(f"  name={s.get('name')!r:25} abbr={s.get('abbreviation')!r:10} value={s.get('value')!r:10} display={s.get('displayValue')!r}")

# Parse all teams
rows = []
groups = data["children"]
for group in groups:
    entries = group.get("standings", {}).get("entries", [])
    for entry in entries:
        team_name = entry["team"]["displayName"]

        # Build stats dict with BOTH name and abbreviation as keys
        stats = {}
        for s in entry["stats"]:
            val = s.get("value")
            if val is None:
                try:
                    val = float(s.get("displayValue", 0))
                except (ValueError, TypeError):
                    val = 0
            if s.get("name"):
                stats[s["name"]] = val
            if s.get("abbreviation"):
                stats[s["abbreviation"]] = val

        rows.append({
            "Team": team_name,
            "MP":   int(stats.get("gamesPlayed",      stats.get("GP",  0))),
            "W":    int(stats.get("wins",              stats.get("W",   0))),
            "D":    int(stats.get("ties",              stats.get("D",   0))),
            "L":    int(stats.get("losses",            stats.get("L",   0))),
            "GF":   int(stats.get("pointsFor",         stats.get("PF",  stats.get("GF", 0)))),
            "GA":   int(stats.get("pointsAgainst",     stats.get("PA",  stats.get("GA", 0)))),
            "GD":   int(stats.get("pointDifferential", stats.get("DIFF",stats.get("GD", 0)))),
            "Pts":  int(stats.get("points",            stats.get("PTS", 0))),
        })
    break  # only first group = overall standings

df = pd.DataFrame(rows)

print(f"\nTeams collected: {len(df)}")
print(f"\nFull standings:")
print(df.to_string(index=False))

# Write tilde-delimited ASCII CSV
df.to_csv(
    output_file,
    sep="~",
    index=False,
    encoding="ascii",
    errors="replace"
)

print(f"\nDone! File saved: {output_file}")
print("Import into Excel via Power Query, set delimiter to tilde (~)")