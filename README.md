# The Urban Pulse: Predicting and Analyzing City Dynamics

**Course:** Data Science | NJIT — Spring 2026  
**Team:** Kush Rank, Serge Lawson, Ibrahim Ragab, Nathaniel Isaac

---

## Overview

This project investigates crime severity patterns across New York City using over 5.6 million NYPD complaint records (2010–2021). The goal is to predict whether a criminal complaint will be classified as a **Felony**, **Misdemeanor**, or **Violation** based on factors like borough, premise type, time of day, and suspect/victim demographics.

---

## Dataset

**NYPD Complaint Data Historic**  
Source: [NYC Open Data](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i)  
Size: ~2.5 GB | ~9.5 million rows | 35 columns

Download the CSV and place it in the project root as:
```
NYPD_Complaint_Data_Historic.csv
```

---

## Project Structure

```
urban-pulse/
├── urban_pulse.ipynb       # Main notebook
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker setup for reproducibility
├── README.md               # This file
└── output/                 # Generated visualizations (created on run)
```

---

## How to Run

### Option 1 — Local (Jupyter)

```bash
# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook urban_pulse.ipynb
```

### Option 2 — Google Colab

Upload the notebook and the dataset CSV to your Google Drive, then open the notebook in Colab and update the file path in the load cell.

### Option 3 — Docker

```bash
# Build the image
docker build -t urban-pulse .

# Run the container
docker run -v $(pwd)/output:/app/output urban-pulse
```

---

## What's Inside the Notebook

| Section | Description |
|---|---|
| 1. Imports | All libraries used |
| 2. Load Data | Efficient loading of only required columns |
| 3. Cleaning | Date parsing, feature engineering, null handling |
| 4. EDA | 10+ charts with interpretations — distributions, trends, bivariate analysis |
| 5. Hypothesis Testing | Chi-Square (borough vs offense level) + T-Test (night vs day felony rate) |
| 6. Machine Learning | Logistic Regression + Random Forest classifier with 5-fold CV |
| 7. Conclusions | Key findings, knowledge discovery, actionable insights, future work |

---

## Key Results

| Model | Accuracy |
|---|---|
| Logistic Regression | ~56% |
| Random Forest | ~60% |
| Random Forest (5-fold CV) | ~59.9% ± 0.12% |

- **H1 (Felony rate vs Borough):** Rejected H0 — Chi-Square p ≈ 0
- **H2 (Felony rate Night vs Day):** Rejected H0 — T-Test p ≈ 0
- **Top predictors:** Premise type and hour of day outperformed demographic features

---

## Future Work

Model accuracy is limited by the absence of ZIP-level socioeconomic data. The following datasets could significantly improve performance if merged on ZIP code:

- [US Census ACS Income & Poverty](https://data.census.gov/table)
- [NYC Opportunity Poverty Data](https://www.nyc.gov/site/opportunity/poverty-in-nyc/poverty-data.page)
- [NYC Population FactFinder](https://popfactfinder.planning.nyc.gov)
- [NYC Child & Community Data](https://data.cccnewyork.org/data/map/66/median-incomes)
- [IRS ZIP Code Income Data (SOI)](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi)

---

## Requirements

See `requirements.txt` for full list. Main dependencies:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
- jupyter
