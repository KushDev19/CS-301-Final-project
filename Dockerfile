FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY urban_pulse.ipynb .

RUN mkdir -p /app/output

CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", \
     "--output", "/app/output/urban_pulse_output.ipynb", \
     "urban_pulse.ipynb"]
