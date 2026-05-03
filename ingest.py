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


def missing(df: pd.DataFrame) -> None:
    counts = df.isnull().sum()
    total = len(df)
    print(f"Missing values (out of {total} rows):\n")
    found = False
    for col, n in counts.items():
        if n > 0:
            print(f"  {col}: {n} missing ({n / total:.1%})")
            found = True
    if not found:
        print("  No missing values.")


def filter_rows(df: pd.DataFrame, column: str, value: str) -> pd.DataFrame:
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found. Available: {list(df.columns)}")
    if pd.api.types.is_numeric_dtype(df[column]):
        try:
            mask = df[column] == float(value)
        except ValueError:
            raise ValueError(f"Column '{column}' is numeric but '{value}' is not a number.")
    else:
        mask = df[column].astype(str).str.lower() == value.lower()
    return df[mask]


def sample(df: pd.DataFrame, n: int = 5, seed: int | None = None) -> None:
    actual = min(n, len(df))
    print(f"Random sample of {actual} row(s) from {len(df)} total:\n")
    print(df.sample(n=actual, random_state=seed).to_string(index=False))


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
