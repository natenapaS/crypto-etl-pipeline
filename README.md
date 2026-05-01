# Crypto ETL Pipeline

A batch ETL pipeline that extracts cryptocurrency market data from CoinGecko API, transforms it, and loads it into a local DuckDB database.

## Architecture

```
CoinGecko API → Extract → Transform → Load → DuckDB
```

## Tech Stack

- **Python 3.10+**
- **Pandas** — data transformation
- **DuckDB** — local analytical database
- **Requests** — HTTP client

## Project Structure

```
crypto-etl-pipeline/
├── etl/
│   ├── extract/        # API fetchers
│   ├── transform/      # Data cleaning & processing
│   └── load/           # Database writers
├── tests/
├── pipeline.py         # Main entry point
└── requirements.txt
```

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/natenapaS/crypto-etl-pipeline.git
cd crypto-etl-pipeline

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the pipeline
python pipeline.py
```

## Sample Output

```
========================================
  Crypto ETL Pipeline
========================================

[1/3] Extracting data...
[Extract] Fetched 5 coins successfully.

[2/3] Transforming data...
[Transform] 5 rows processed.

[3/3] Loading data...
[Load] Database initialized.
[Load] Saved successfully. Total rows in database: 5

Pipeline completed successfully.
```