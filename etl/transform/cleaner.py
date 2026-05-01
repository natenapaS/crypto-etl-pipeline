import pandas as pd
from datetime import datetime, timezone

def clean_prices(raw_data: list) -> pd.DataFrame:
    """
    Transform raw CoinGecko data into a clean DataFrame.

    Args:
        raw_data: Raw list of coin dicts from CoinGecko API

    Returns:
        Cleaned pandas DataFrame
    """
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
    df = df.dropna(subset=["price_usd"])

    print(f"[Transform] {len(df)} rows processed.")
    print(df.to_string(index=False))
    return df


if __name__ == "__main__":
    from etl.extract.coingecko import fetch_prices

    raw = fetch_prices(["bitcoin", "ethereum", "solana"])
    df = clean_prices(raw)