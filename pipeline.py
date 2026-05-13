import os
from etl.extract.coingecko import fetch_prices
from etl.transform.cleaner import clean_prices
from etl.transform.validator import validate_prices
from etl.load.database import init_db, save_prices
# from etl.logger import get_logger

# logger = get_logger(__name__)

COINS = ["bitcoin", "ethereum", "solana", "cardano", "dogecoin"]

def run():
    print("=" * 40)
    print("Crypto ETL Pipeline started.")
    print("=" * 40)

    os.makedirs("data", exist_ok=True)

    try:
        print("[1/3] Extracting data...")
        raw = fetch_prices(COINS)

        print("[2/3] Transforming data...")
        df = clean_prices(raw)
        validate_prices(df, expected_coins=COINS)

        print("[3/3] Loading data...")
        init_db()
        save_prices(df)

        print("Pipeline completed successfully.")

    except Exception as e:
        print(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run()