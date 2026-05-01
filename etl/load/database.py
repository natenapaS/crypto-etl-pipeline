import duckdb
import pandas as pd

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
    print("[Load] Database initialized.")

def save_prices(df: pd.DataFrame):
    """Insert a DataFrame into the crypto_prices table."""
    con = duckdb.connect(DB_PATH)
    con.execute("INSERT INTO crypto_prices SELECT * FROM df")
    total = con.execute("SELECT COUNT(*) FROM crypto_prices").fetchone()[0]
    con.close()
    print(f"[Load] Saved successfully. Total rows in database: {total}")


if __name__ == "__main__":
    import os
    os.makedirs("data", exist_ok=True)

    from etl.extract.coingecko import fetch_prices
    from etl.transform.cleaner import clean_prices

    init_db()
    raw = fetch_prices(["bitcoin", "ethereum", "solana"])
    df = clean_prices(raw)
    save_prices(df)