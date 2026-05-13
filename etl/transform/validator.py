import pandas as pd

from etl import logger
from etl.logger import get_logger
# from etl.logger import get_logger

# logger = get_logger(__name__)       

def validate_prices(df: pd.DataFrame, expected_coins: list) -> bool:
    """
    Validate data quality before loading.

    Checks:
    - No missing required fields
    - Price must be greater than 0
    - All expected coins are present
    - No duplicate coin entries

    Returns:
        True if all checks pass, raises Exception if any check fails
    """
    passed = True

    # Check 1: Required columns exist
    required_columns = ["coin_id", "symbol", "price_usd", "market_cap", "volume_24h", "fetched_at"]
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise Exception(f"[Quality Check] Missing columns: {missing_cols}")
    print("[Quality Check] Required columns: PASSED")

    # Check 2: No null values in required fields
    null_counts = df[required_columns].isnull().sum()
    if null_counts.any():
        print(f"[Quality Check] Null values found:\n{null_counts[null_counts > 0]}")
        passed = False
    else:
        print("[Quality Check] No null values: PASSED")

    # Check 3: Price must be > 0
    invalid_prices = df[df["price_usd"] <= 0]
    if not invalid_prices.empty:
        print(f"[Quality Check] Invalid prices found:\n{invalid_prices[['coin_id', 'price_usd']]}")
        passed = False
    else:
        print("[Quality Check] Price values: PASSED")

    # Check 4: All expected coins are present
    missing_coins = [c for c in expected_coins if c not in df["coin_id"].values]
    if missing_coins:
        print(f"[Quality Check] Missing coins: {missing_coins}")
        passed = False
    else:
        print("[Quality Check] All expected coins present: PASSED")

    # Check 5: No duplicates
    duplicates = df[df.duplicated(subset=["coin_id"])]
    if not duplicates.empty:
        print(f"[Quality Check] Duplicate entries found: {duplicates['coin_id'].tolist()}")
        passed = False
    else:
        print("[Quality Check] No duplicates: PASSED")

    if not passed:
        raise Exception("[Quality Check] Data quality checks failed. Aborting load.")

    print("[Quality Check] All checks passed.")
    return True