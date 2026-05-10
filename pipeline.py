import os
from etl.extract.coingecko import fetch_prices
from etl.transform.cleaner import clean_prices
from etl.load.database import init_db, save_prices
from etl.logger import get_logger

logger = get_logger(__name__)

COINS = ["bitcoin", "ethereum", "solana", "cardano", "dogecoin"]

def run():
    logger.info("=" * 40)
    logger.info("Crypto ETL Pipeline started.")
    logger.info("=" * 40)

    os.makedirs("data", exist_ok=True)

    try:
        logger.info("[1/3] Extracting data...")
        raw = fetch_prices(COINS)

        logger.info("[2/3] Transforming data...")
        df = clean_prices(raw)

        logger.info("[3/3] Loading data...")
        init_db()
        save_prices(df)

        logger.info("Pipeline completed successfully.")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run()