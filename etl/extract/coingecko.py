import requests
import time
from etl.logger import get_logger

logger = get_logger(__name__)

MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

def fetch_prices(coin_ids: list, vs_currency: str = "usd") -> list:
    """
    Fetch crypto market data from CoinGecko API with retry logic.

    Args:
        coin_ids: List of coin IDs e.g. ["bitcoin", "ethereum"]
        vs_currency: Target currency (default: "usd")

    Returns:
        List of raw market data dicts
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": vs_currency,
        "ids": ",".join(coin_ids),
        "order": "market_cap_desc",
        "sparkline": False,
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(f"Fetching data (attempt {attempt}/{MAX_RETRIES})...")
            response = requests.get(url, params=params, timeout=10)

            if response.status_code != 200:
                raise Exception(f"API Error: {response.status_code} - {response.text}")

            data = response.json()

            if not data:
                raise ValueError("API returned empty data.")

            logger.info(f"Fetched {len(data)} coins successfully.")
            return data

        except Exception as e:
            logger.warning(f"Attempt {attempt} failed: {e}")
            if attempt < MAX_RETRIES:
                logger.info(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                logger.error("All retry attempts exhausted.")
                raise