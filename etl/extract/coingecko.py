import requests

def fetch_prices(coin_ids: list, vs_currency: str = "usd") -> list:
    """
    Fetch crypto market data from CoinGecko API.
    
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

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

    data = response.json()
    print(f"[Extract] Fetched {len(data)} coins successfully.")
    return data


if __name__ == "__main__":
    coins = ["bitcoin", "ethereum", "solana"]
    result = fetch_prices(coins)

    for coin in result:
        print(f"{coin['name']}: ${coin['current_price']:,}")