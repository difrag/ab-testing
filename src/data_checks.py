from __future__ import annotations

import pandas as pd

from src.config import RAW_DATA_PATH


EXPECTED_COLUMNS = [
    "recency",
    "history_segment",
    "history",
    "mens",
    "womens",
    "zip_code",
    "newbie",
    "channel",
    "segment",
    "visit",
    "conversion",
    "spend",
]


def load_raw_data(path=RAW_DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def validate_raw_data(df: pd.DataFrame) -> dict[str, object]:
    """Return simple data quality checks for the raw experiment file."""
    missing_columns = sorted(set(EXPECTED_COLUMNS) - set(df.columns))
    extra_columns = sorted(set(df.columns) - set(EXPECTED_COLUMNS))

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_columns": missing_columns,
        "extra_columns": extra_columns,
        "missing_values": df.isna().sum().to_dict(),
        "segments": sorted(df["segment"].dropna().unique().tolist()),
        "zip_code_values": sorted(df["zip_code"].dropna().unique().tolist()),
    }


if __name__ == "__main__":
    raw = load_raw_data()
    checks = validate_raw_data(raw)
    for key, value in checks.items():
        print(f"{key}: {value}")
