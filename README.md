# Crypto ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.13-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-orange)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A batch ETL pipeline that extracts cryptocurrency market data from CoinGecko API, transforms and validates it, then loads it into a DuckDB database.

## Architecture

```
CoinGecko API → Extract → Transform → Validate → Load → DuckDB
```

## Features

- Extracts real-time market data for multiple cryptocurrencies
- Cleans and transforms raw API data using Pandas
- Validates data quality before loading (null checks, price checks, duplicate checks)
- Retry logic with up to 3 attempts on API failure
- Automated scheduling (runs every hour)
- Fully containerized with Docker
- Unit tested with pytest

## Tech Stack

- **Python 3.13**
- **Pandas** — data transformation
- **DuckDB** — local analytical database
- **Requests** — HTTP client
- **Schedule** — job scheduling
- **Docker** — containerization
- **pytest** — unit testing

## Project Structure

```
crypto-etl-pipeline/
├── etl/
│   ├── extract/
│   │   └── coingecko.py    # CoinGecko API fetcher
│   ├── transform/
│   │   ├── cleaner.py      # Data cleaning & transformation
│   │   └── validator.py    # Data quality checks
│   └── load/
│       └── database.py     # DuckDB writer
├── tests/
│   └── test_transformer.py # Unit tests
├── pipeline.py             # Main entry point
├── scheduler.py            # Automated scheduling
├── Dockerfile
└── requirements.txt
```

## Getting Started

### Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/natenapaS/crypto-etl-pipeline.git
cd crypto-etl-pipeline

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the pipeline
python pipeline.py
```

### Run with Docker

```bash
# Build the image
docker build -t crypto-etl-pipeline .

# Run the pipeline
docker run crypto-etl-pipeline
```

### Run Tests

```bash
pytest tests/ -v
```

## Sample Output

```
========================================
Crypto ETL Pipeline started.
========================================
[1/3] Extracting data...
Fetching data (attempt 1/3)...
Fetched 5 coins successfully.
[2/3] Transforming data...
[Transform] 5 rows processed.
[Quality Check] Required columns: PASSED
[Quality Check] No null values: PASSED
[Quality Check] Price values: PASSED
[Quality Check] All expected coins present: PASSED
[Quality Check] No duplicates: PASSED
[Quality Check] All checks passed.
[3/3] Loading data...
Database initialized.
Saved successfully. Total rows in database: 5
Pipeline completed successfully.
```

## Coins Tracked

| Coin | Symbol |
|------|--------|
| Bitcoin | BTC |
| Ethereum | ETH |
| Solana | SOL |
| Cardano | ADA |
| Dogecoin | DOGE |

## License

MIT