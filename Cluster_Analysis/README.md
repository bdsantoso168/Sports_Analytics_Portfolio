# Baseball Player Cluster Analysis

**Course:** ISOM 232 — Sports Analytics In Action
**Author:** Benedict Daxell Santoso | Suffolk University

> Segment 143 MLB players into performance tiers using two unsupervised learning methods — Hierarchical (Ward's linkage) and K-means — then profile each cluster by key batting statistics.

<img width="2880" height="1472" alt="cluster_analysis_banner" src="https://github.com/user-attachments/assets/6e657f63-db65-4f4c-99a8-a8d617ddfb7a" />

---

## Dataset

| File | Rows | Source |
|---|---|---|
| `Baseball.csv` | 143 players | Course-provided MLB batting dataset |

**Variables used for clustering (9 total):** Games, AtBats, Runs, Hits, HR, RBI, AVG, OBP, SLG

All variables were standardized to a **0 to 1 range** (min-max rescaling) before clustering so that volume stats like AtBats do not dominate AVG-scale metrics.

---

## Methods

### Model 1 — Hierarchical Clustering (Ward's Linkage)

| Setting | Value |
|---|---|
| Algorithm | Agglomerative hierarchical |
| Linkage | Ward's method |
| Distance measure | Squared Euclidean |
| Standardization | Range 0 to 1 |
| Clusters saved | 3 (`CLU3_1`) |
| Output | Dendrogram + icicle plot + agglomeration schedule |

Ward's method merges clusters in a way that minimizes within-cluster variance at each step, producing compact and comparably sized groups that are easy to interpret.

### Model 2 — K-Means Clustering

| Setting | Value |
|---|---|
| Algorithm | K-Means (iterate and classify) |
| Number of clusters | 3 |
| Max iterations | 10 |
| Convergence | Achieved at iteration 7 (max change = 0.000) |
| Columns saved | `QCL_1` (membership) + `QCL_2` (distance from center) |

K-means starts from three initial seed observations and iterates centroids until members stop reassigning. The minimum distance between initial centers was 140.933, confirming good separation of seeds.

---

## Results

### Hierarchical Model — Cluster Sizes

| Cluster | Count |
|---|---|
| 1 | varies (see Excel workbook) |
| 2 | varies |
| 3 | varies |

The dendrogram shows three visually distinct branches, with the largest split occurring at rescaled distance ~37 and the final merge at ~57.

### K-Means Model — Final Cluster Centers

| Stat | Cluster 1 | Cluster 2 | Cluster 3 |
|---|---|---|---|
| Games | 146 | 135 | 155 |
| AtBats | 545 | 481 | 608 |
| Runs | 70 | 58 | 85 |
| Hits | 148 | 122 | 171 |
| HR | 18 | 13 | 17 |
| RBI | 71 | 57 | 75 |
| AVG | .272 | .254 | .282 |
| OBP | .337 | .323 | .340 |
| SLG | .434 | .395 | .431 |
| **Count** | **53** | **49** | **41** |

**Cluster 3 — High-Volume Contact Hitters (n = 41)**
Most at-bats (608), most runs (85), highest hits (171), and best AVG (.282) and OBP (.340). These are everyday starters who get on base consistently.

**Cluster 1 — Mid-Tier Power Hitters (n = 53)**
Above-average volume and the highest HR rate (18) relative to their size group. Solid contributors who hit with more power than the contact cluster.

**Cluster 2 — Lower-Tier / Part-Time Players (n = 49)**
Fewest games (135), lowest across nearly all offensive metrics. Likely bench players, platoon starters, or players with injury-limited seasons.

### ANOVA Significance (K-Means)

All nine clustering variables are statistically significant (p < .05), with AtBats (F = 410.35), Hits (F = 141.40), and Games (F = 90.82) showing the strongest separation between clusters. AVG (F = 15.51) and SLG (F = 7.34) also differ meaningfully across groups despite their narrow numerical range.

### Distances Between K-Means Final Cluster Centers

| | Cluster 1 | Cluster 2 | Cluster 3 |
|---|---|---|---|
| Cluster 1 | — | 73.3 | 69.4 |
| Cluster 2 | 73.3 | — | 142.1 |
| Cluster 3 | 69.4 | 142.1 | — |

Clusters 2 and 3 are the most distant from each other (142.1), confirming they represent the two performance extremes. Clusters 1 and 3 are the closest pair, consistent with both containing everyday starters.

---

## Model Comparison

| Dimension | Hierarchical (Ward's) | K-Means |
|---|---|---|
| Cluster sizes | Uneven (Ward's typical) | More balanced (53/49/41) |
| Interpretability | Tree structure makes merges visible | Centroid profiles are directly readable |
| Stability | Deterministic | Depends on seed initialization |
| Best for | Exploring unknown structure | Confirming a 3-group hypothesis |

Both models broadly agree that the data separates into a high-performance everyday-starter tier, a mid-tier power-oriented group, and a lower-volume bench/platoon group. K-means produces more balanced cluster sizes and directly interpretable centroids, making it slightly more actionable for player segmentation. The hierarchical dendrogram is more useful for understanding how players relate to one another at different levels of similarity.

---

## Repository Structure

```
Cluster_Analysis/
├── README.md                        (this file)
├── .gitignore
├── data/
│   └── Baseball.csv                 (143-player MLB batting dataset)
├── spss/
│   ├── Hierarchical.sav             (SPSS data file after hierarchical run)
│   ├── Kmeans.sav                   (SPSS data file after K-means run)
│   └── Results.spv                  (SPSS output viewer: agglomeration schedule, dendrogram, ANOVA)
└── output/
    └── BDS_ClusterAnalysis.xlsx     (final submission workbook: Hierarchical + K-means + Compare sheets)
    └── Clustering_Output.pdf        (full SPSS output: agglomeration 
```

---

## Tools

| Tool | Version | Purpose |
|---|---|---|
| IBM SPSS Statistics | 29 | Hierarchical clustering, K-means, dendrogram generation |
| Microsoft Excel | 365 | Cluster assignment paste-in, COUNTIF/AVERAGEIF profiling, submission workbook |

---

## Key Concepts Demonstrated

**Why standardize 0 to 1?** AtBats ranges in the hundreds while AVG sits near 0.250. Without rescaling, volume stats would dominate the Euclidean distance calculation and absorb all the signal from rate stats.

**Why Ward's method?** Ward's minimizes within-cluster variance at each merge, producing compact groups. It is the most common linkage for sports analytics segmentation because the resulting clusters tend to be interpretable as performance tiers.

**Why 3 clusters?** The dendrogram shows a clear three-branch structure before distance values escalate sharply, making three a natural and well-supported choice.

---

## Disclaimer

This project was completed as part of coursework in ISOM 232 — Sports Analytics In Action at Suffolk University. All data was provided for instructional purposes. Results are not intended for real-world scouting, roster decisions, or commercial use.
