import pandas as pd

# Original dataset is 2.5GB (~9.5M rows)
# We truncate to 50,000 rows for the Docker demo
# Full dataset: https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i

USE_COLS = [
    'CMPLNT_FR_DT', 'CMPLNT_FR_TM',
    'LAW_CAT_CD', 'BORO_NM',
    'OFNS_DESC', 'PREM_TYP_DESC',
    'CRM_ATPT_CPTD_CD', 'LOC_OF_OCCUR_DESC',
    'SUSP_AGE_GROUP', 'SUSP_RACE', 'SUSP_SEX',
    'VIC_AGE_GROUP', 'VIC_RACE', 'VIC_SEX'
]

print("Reading full dataset...")
df = pd.read_csv(
    'NYPD_Complaint_Data_Historic.csv',
    usecols=USE_COLS,
    low_memory=False,
    nrows=50000
)

print(f"Loaded {len(df):,} rows")
df.to_csv('NYPD_sample.csv', index=False)
print("Saved as NYPD_sample.csv — ready for Docker and GitHub")
print(f"File size is roughly {df.memory_usage(deep=True).sum() / 1024 / 1024:.1f} MB in memory")