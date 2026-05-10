import pandas as pd
from datetime import datetime, timezone
from etl.logger import get_logger

logger = get_logger(__name__)

def clean_prices(raw_data: list) -> pd.DataFrame:
    """
    Transform raw CoinGecko data into a clean DataFrame.

    Args:
        raw_data: Raw list of coin dicts from CoinGecko API

    Returns:
        Cleaned pandas DataFrame
    """
    if not raw_data:
        raise ValueError("No data to transform.")

    records = []

    for coin in raw_data:
        records.append({
            "coin_id":        coin["id"],
            "symbol":         coin["symbol"].upper(),
            "name":           coin["name"],
            "price_usd":      coin["current_price"],
            "market_cap":     coin["market_cap"],
            "volume_24h":     coin["total_volume"],
            "change_24h_pct": coin["price_change_percentage_24h"],
            "fetched_at":     datetime.now(timezone.utc).isoformat(),
        })

    df = pd.DataFrame(records)
    before = len(df)
    df = df.dropna(subset=["price_usd"])
    dropped = before - len(df)

    if dropped > 0:
        logger.warning(f"Dropped {dropped} rows with missing price.")

    logger.info(f"{len(df)} rows processed.")
    return df