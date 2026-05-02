FROM python:3.11-slim

# Full dataset is 2.5GB (9.5M rows) — too large for GitHub/Docker
# We use a 50,000-row sample (NYPD_sample.csv) for reproducibility
# Full data: https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY NYPD_sample.csv .
COPY urban_pulse.ipynb .

RUN mkdir -p /app/output

CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", \
     "--ExecutePreprocessor.timeout=600", \
     "--output", "/app/output/urban_pulse_output.ipynb", \
     "urban_pulse.ipynb"]