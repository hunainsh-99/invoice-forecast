# Invoice-Forecast

A complete pipeline for cleaning, aggregating, and forecasting monthly revenue for Argas and BGP invoices, with an interactive Streamlit dashboard.

---

## Features

- **Data Cleaning** (`src/clean.py`):  

  Reads raw Excel (`InvoiceList.xlsx`), normalizes columns, parses dates, casts amounts to numeric, writes `invoices_clean.parquet`.

- **Feature Engineering** (`src/features.py`):  

  Computes days-open, aging buckets, and late-payment labels, saves `features.parquet`.

- **Aggregation** (`src/aggregate.py`):  

  Filters to **ARGAS** and **BGP**, sums monthly and yearly totals, writes `monthly_totals.csv` and `yearly_totals.csv`.

- **Forecasting** (`src/forecast_revenue.py`):  

  Uses Prophet to generate a 12-month revenue forecast per company, writes `revenue_forecast.csv`.

- **Visualization**:  

  - Static plots: `monthly_revenue.png`, `yearly_revenue.png`, `rev_history_forecast.png`

  - **Interactive Streamlit Dashboard** (`app.py`): Company selection, dynamic plots, and data tables.

---

## Business Impact

Forecasting future invoice revenue helps organizations plan cash flow, allocate budgets, and optimize staffing.  
This project simulates a real-world financial reporting and forecasting workflow that supports data-driven decision-making across finance and operations.

---

## Tech Stack

- **Python 3.10+**
- **Data Processing**: pandas, pyarrow, openpyxl
- **Forecasting**: Prophet
- **Visualization**: matplotlib
- **Web UI**: Streamlit

---

## Installation

Clone the repository and set up the environment:

```bash
git clone git@github.com:hunainsh-99/invoice-forecast.git
cd invoice-forecast

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

Usage

Step 1: Clean raw invoice data

bash
Copy
Edit
python src/clean.py

Step 2: Build feature table (optional)

bash
Copy
Edit
python src/features.py

Step 3: Aggregate monthly and yearly totals

bash
Copy
Edit
python src/aggregate.py

Step 4: Generate 12-month revenue forecast

bash
Copy
Edit
python src/forecast_revenue.py

Step 5: Produce static charts

bash
Copy
Edit
python src/plot_aggregates.py
python src/plot_forecast.py

Step 6: Launch the Streamlit dashboard

bash
Copy
Edit
streamlit run app.py


Project Structure

invoice-forecast/
│
├── data/
│   ├── InvoiceList.xlsx           # Raw invoice export
│   ├── invoices_clean.parquet     # Cleaned dataset
│   ├── features.parquet           # Engineered features
│   ├── monthly_totals.csv         # Aggregated monthly revenue
│   ├── yearly_totals.csv          # Aggregated yearly revenue
│   └── revenue_forecast.csv       # 12-month Prophet forecast
│
├── .venv/                         # Python virtual environment
├── requirements.txt               # Pinned Python dependencies
│
├── src/
│   ├── clean.py                   # Clean raw Excel
│   ├── features.py                # Engineer features
│   ├── aggregate.py               # Monthly/yearly aggregation
│   ├── forecast_revenue.py        # Prophet-based forecasting
│   ├── plot_aggregates.py          # Static revenue plots
│   └── plot_forecast.py            # Static forecast visualization
│
├── app.py                         # Streamlit dashboard
├── monthly_revenue.png            # Example output plot
├── yearly_revenue.png             # Example output plot
├── rev_history_forecast.png       # Example output plot
└── README.md                      # ← You are here
