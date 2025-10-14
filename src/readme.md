# Python Scripts for Energy Production and Coverage Analysis (2005-2023)
## Overview
This repository contains Python scripts designed to process, analyze, and visualize data related to electricity production and coverage in Italy from 2005 to 2023. The scripts leverage libraries such as pandas, matplotlib, and seaborn to clean data, merge datasets, and generate insights.
## Scripts
### 1. Data Cleaning and Merging Script (1_data_clean_merge.py)
Script to load, clean, and merge production and coverage datasets into a unified dataset with calculated metrics.
#### Functionality:
- Loads 2005-2023_prod.csv and 2005-2023_cover.csv from specified paths.
- Cleans data by removing NaN values, invalid entries, and standardizing column types (e.g., converting Anno to integer).
- Replaces energy source categories (e.g., "Termoelettrico" to "Geotermoelettrico", "Idrico tradizionale" to "Idrico").
- Filters out irrelevant categories like "Saldo import/export" and "Bioenergie" from coverage data.
- Groups data by year, region, and source, then performs an inner merge.
- Calculates SaldoEnergetico (production - coverage) and Tasso_copertura(%) (coverage as a percentage of production).


- Output: Generates merge_produzione_copertura_con_tasso.csv and merge_produzione_copertura_con_tasso.xlsx files.
- Dependencies: pandas, matplotlib, seaborn, numpy.

### 2. Production Analysis Script (edaproduzione.py)

Script for exploratory data analysis (EDA) and visualization of electricity production data.
#### Functionality:
- Loads 2005-2023_prod.csv for analysis.
- Provides descriptive statistics by source and region.
- Generates visualizations including:
- Trend over time for production by source (line plot).
- Trend over time for total production by region (line plot).
- Boxplot of production distribution by source and region.
- Heatmap of production by region and year.
- Percentage contribution of each source per year (line plot).




- Output: Displays plots and prints statistical summaries.
- Dependencies: pandas, matplotlib, seaborn.

### 3. Coverage Analysis Script (edacopertura.py)

Script for exploratory data analysis (EDA) and visualization of electricity coverage data.
#### Functionality:
- Loads 2005-2023.csv and prod2025.csv for analysis.
- Provides descriptive statistics by source and region.
- Generates visualizations including:
- Trend over time for coverage by source (line plot).
- Trend over time for total coverage by region (line plot).
- Boxplot of coverage distribution by source and region.
- Heatmap of coverage by region and year.
- Percentage contribution of each source per year (line plot).




- Output: Displays plots and prints statistical summaries.
- Dependencies: pandas, matplotlib, seaborn.
