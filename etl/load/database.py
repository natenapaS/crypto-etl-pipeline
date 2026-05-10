import duckdb
import pandas as pd
from etl.logger import get_logger

logger = get_logger(__name__)

DB_PATH = "data/crypto.duckdb"

def init_db():
    """Initialize the database and create tables if they don't exist."""
    con = duckdb.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            coin_id        VARCHAR,
            symbol         VARCHAR,
            name           VARCHAR,
            price_usd      DOUBLE,
            market_cap     DOUBLE,
            volume_24h     DOUBLE,
            change_24h_pct DOUBLE,
            fetched_at     TIMESTAMP
        )
    """)
    con.close()
    logger.info("Database initialized.")

def save_prices(df: pd.DataFrame):
    """Insert a DataFrame into the crypto_prices table."""
    if df.empty:
        raise ValueError("DataFrame is empty. Nothing to save.")

    con = duckdb.connect(DB_PATH)
    con.execute("INSERT INTO crypto_prices SELECT * FROM df")
    total = con.execute("SELECT COUNT(*) FROM crypto_prices").fetchone()[0]
    con.close()
    logger.info(f"Saved successfully. Total rows in database: {total}")