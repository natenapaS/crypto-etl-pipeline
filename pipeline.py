from etl.extract.coingecko import fetch_prices
from etl.transform.cleaner import clean_prices
from etl.load.database import init_db, save_prices
import os

COINS = ["bitcoin", "ethereum", "solana", "cardano", "dogecoin"]

def run():
    print("=" * 40)
    print("  Crypto ETL Pipeline")
    print("=" * 40)

    os.makedirs("data", exist_ok=True)

    print("\n[1/3] Extracting data...")
    raw = fetch_prices(COINS)

    print("\n[2/3] Transforming data...")
    df = clean_prices(raw)

    print("\n[3/3] Loading data...")
    init_db()
    save_prices(df)

    print("\nPipeline completed successfully.")

if __name__ == "__main__":
    run()