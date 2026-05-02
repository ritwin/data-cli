from __future__ import annotations

import pandas as pd
from pathlib import Path


def load_csv(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"No file found at {file_path}")
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a .csv file, got {path.suffix}")
    return pd.read_csv(path)


def inspect(df: pd.DataFrame) -> None:
    print(f"Rows:    {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"\nColumn names and types:")
    for col, dtype in df.dtypes.items():
        print(f"  {col}: {dtype}")
    print(f"\nFirst 5 rows:")
    print(df.head())


def summarise(df: pd.DataFrame, column: str) -> None:
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found. Available: {list(df.columns)}")

    series = df[column]

    if pd.api.types.is_numeric_dtype(series):
        print(f"Column: {column} (numeric)")
        print(series.describe().to_string())
    else:
        print(f"Column: {column} (categorical)")
        print(series.value_counts().to_string())
