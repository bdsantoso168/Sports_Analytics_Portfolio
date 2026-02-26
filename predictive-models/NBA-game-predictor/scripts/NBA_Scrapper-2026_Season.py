#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:09:54 2026

@author: benedictsantoso
"""
import csv
import time
import requests
from bs4 import BeautifulSoup

URL = "https://www.basketball-reference.com/leagues/NBA_2026_games.html"
OUTFILE = "NBA_2026_Results.csv"

def clean(text: str) -> str:
    """Normalize whitespace."""
    return " ".join(text.split()).strip()

def main():
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # The season page links to each month page under the "Games" section.
    # Example href: /leagues/NBA_2026_games-october.html
    month_links = []
    for a in soup.select('a[href*="/leagues/NBA_2026_games-"]'):
        href = a.get("href")
        if href and href.endswith(".html") and href not in month_links:
            month_links.append(href)

    # Fallback: if month links aren't found, try scraping tables on the main page (rare)
    if not month_links:
        month_links = ["/leagues/NBA_2026_games.html"]

    with open(OUTFILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="~")
        writer.writerow(["Date", "Home Team", "Away Team", "Home Points", "Away Points"])

        for href in month_links:
            page_url = "https://www.basketball-reference.com" + href
            r = requests.get(page_url, headers={"User-Agent": "Mozilla/5.0"})
            r.raise_for_status()
            psoup = BeautifulSoup(r.text, "html.parser")

            table = psoup.find("table", id="schedule")
            if not table:
                continue

            for tr in table.select("tbody tr"):
                # Skip divider/header rows that sometimes appear inside tbody
                if "class" in tr.attrs and "thead" in tr["class"]:
                    continue

                date_cell = tr.find("th", {"data-stat": "date_game"})
                visitor = tr.find("td", {"data-stat": "visitor_team_name"})
                home = tr.find("td", {"data-stat": "home_team_name"})
                pts_away = tr.find("td", {"data-stat": "visitor_pts"})
                pts_home = tr.find("td", {"data-stat": "home_pts"})

                if not (date_cell and visitor and home and pts_away and pts_home):
                    continue

                date = clean(date_cell.get_text())
                away_team = clean(visitor.get_text())
                home_team = clean(home.get_text())
                away_points = clean(pts_away.get_text())
                home_points = clean(pts_home.get_text())

                # Skip games not played yet (no scores)
                if away_points == "" or home_points == "":
                    continue

                writer.writerow([date, home_team, away_team, home_points, away_points])

            time.sleep(0.5)  # polite delay

    print(f"Saved: {OUTFILE}")

if __name__ == "__main__":
    main()
