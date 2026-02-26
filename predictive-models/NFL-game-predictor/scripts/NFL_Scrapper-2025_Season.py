#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:22:16 2026

@author: benedictsantoso
"""

# ------------------------------------------------------------
# ISOM 232 - NFL 2025 Screen Scraper
# File: NFLWeeklyResults.py
# Output: NFL2025Results.csv
# ------------------------------------------------------------

# import packages
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

# 1) Connect to the webpage (NFL 2025 schedule & results)
source = urllib.request.urlopen(
    "https://www.pro-football-reference.com/years/2025/games.htm"
)

# 2) Parse HTML into BeautifulSoup
soup = BeautifulSoup(source, "html.parser")

# 3) Process web data (grab the first table, then loop rows/cells)
scoretab = soup.find("table")   # first table on the page
dataoutput = ""                 # collect all rows into one big string

for tr in scoretab.find_all("tr"):
    standdata = ""  # one row at a time

    # grab BOTH td and th so you also get headers / week labels if present
    for cell in tr.find_all(["td", "th"]):
        standdata = standdata + "~" + cell.text

    # only add non-empty rows (prevents blank lines)
    if standdata.strip() != "":
        dataoutput = dataoutput + "\n" + standdata

# 4) Write the scraped data to a CSV text file (bytes / ASCII / ignore errors)
fileName = "NFL2025Results.csv"
fout = open(os.path.expanduser(fileName), "wb")  # creates file if it doesn't exist
fout.write(bytes(dataoutput, encoding="ascii", errors="ignore"))
fout.close()

print("DONE - Created:", fileName)
