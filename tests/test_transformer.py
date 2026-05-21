import pandas as pd
import pytest
from etl.transform.cleaner import clean_prices
from etl.transform.validator import validate_prices


# ---- Fixtures ----

@pytest.fixture
def sample_raw_data():
    return [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 80000,
            "market_cap": 1500000000000,
            "total_volume": 40000000000,
            "price_change_percentage_24h": 1.5,
        },
        {
            "id": "ethereum",
            "symbol": "eth",
            "name": "Ethereum",
            "current_price": 2000,
            "market_cap": 250000000000,
            "total_volume": 15000000000,
            "price_change_percentage_24h": -0.5,
        },
    ]


# ---- clean_prices tests ----

def test_clean_prices_returns_dataframe(sample_raw_data):
    df = clean_prices(sample_raw_data)
    assert isinstance(df, pd.DataFrame)

def test_clean_prices_correct_columns(sample_raw_data):
    df = clean_prices(sample_raw_data)
    expected = ["coin_id", "symbol", "name", "price_usd",
                "market_cap", "volume_24h", "change_24h_pct", "fetched_at"]
    assert list(df.columns) == expected

def test_clean_prices_symbol_uppercase(sample_raw_data):
    df = clean_prices(sample_raw_data)
    assert df["symbol"].tolist() == ["BTC", "ETH"]

def test_clean_prices_drops_null_price():
    raw = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": None,
            "market_cap": 1500000000000,
            "total_volume": 40000000000,
            "price_change_percentage_24h": 1.5,
        }
    ]
    df = clean_prices(raw)
    assert len(df) == 0

def test_clean_prices_empty_input():
    with pytest.raises(ValueError):
        clean_prices([])


# ---- validate_prices tests ----

def test_validate_passes_with_good_data(sample_raw_data):
    df = clean_prices(sample_raw_data)
    result = validate_prices(df, expected_coins=["bitcoin", "ethereum"])
    assert result is True

def test_validate_fails_with_negative_price(sample_raw_data):
    df = clean_prices(sample_raw_data)
    df.loc[0, "price_usd"] = -100
    with pytest.raises(Exception):
        validate_prices(df, expected_coins=["bitcoin", "ethereum"])

def test_validate_fails_with_missing_coin(sample_raw_data):
    df = clean_prices(sample_raw_data)
    with pytest.raises(Exception):
        validate_prices(df, expected_coins=["bitcoin", "ethereum", "solana"])

def test_validate_fails_with_duplicates(sample_raw_data):
    df = clean_prices(sample_raw_data)
    df = pd.concat([df, df]).reset_index(drop=True)
    with pytest.raises(Exception):
        validate_prices(df, expected_coins=["bitcoin", "ethereum"])