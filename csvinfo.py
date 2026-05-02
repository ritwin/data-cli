import argparse
import csv


def load(path: str) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def summarize(rows: list[dict]) -> None:
    if not rows:
        print("Empty file.")
        return
    columns = list(rows[0].keys())
    print(f"Rows   : {len(rows)}")
    print(f"Columns: {len(columns)}")
    print(f"Headers: {', '.join(columns)}")
    print()
    for col in columns:
        values = [r[col] for r in rows]
        try:
            nums = [float(v) for v in values]
            print(f"  {col}: min={min(nums):.2f}  max={max(nums):.2f}  mean={sum(nums)/len(nums):.2f}")
        except ValueError:
            unique = len(set(values))
            print(f"  {col}: {unique} unique values")


def main() -> None:
    parser = argparse.ArgumentParser(description="Quick CSV inspector")
    parser.add_argument("file", help="Path to CSV file")
    args = parser.parse_args()
    rows = load(args.file)
    summarize(rows)


if __name__ == "__main__":
    main()
