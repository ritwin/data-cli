from __future__ import annotations

import argparse
from ingest import load_csv, inspect, summarise, missing, filter_rows, sample


def main() -> None:
    parser = argparse.ArgumentParser(description="data-cli: explore CSVs from the command line")
    subparsers = parser.add_subparsers(dest="command")

    inspect_parser = subparsers.add_parser("inspect", help="Print basic info about a CSV")
    inspect_parser.add_argument("--file", required=True, help="Path to CSV file")
    inspect_parser.add_argument("--limit", type=int, default=5, help="Rows to preview (default: 5)")

    summarise_parser = subparsers.add_parser("summarise", help="Summarise a specific column")
    summarise_parser.add_argument("--file", required=True)
    summarise_parser.add_argument("--column", required=True)

    missing_parser = subparsers.add_parser("missing", help="Show columns with missing values")
    missing_parser.add_argument("--file", required=True)
    missing_parser.add_argument("--all", action="store_true", help="Show all columns, including complete ones")

    sample_parser = subparsers.add_parser("sample", help="Show N random rows")
    sample_parser.add_argument("--file", required=True)
    sample_parser.add_argument("--n", type=int, default=5, help="Number of rows (default: 5)")
    sample_parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")

    filter_parser = subparsers.add_parser("filter", help="Filter rows by column value")
    filter_parser.add_argument("--file", required=True)
    filter_parser.add_argument("--column", required=True)
    filter_parser.add_argument("--value", required=True)
    filter_parser.add_argument("--limit", type=int, default=10, help="Max rows to show (default: 10)")
    filter_parser.add_argument("--output", default=None, help="Save matched rows to this CSV file")

    args = parser.parse_args()

    if args.command == "inspect":
        try:
            df = load_csv(args.file)
            inspect(df, limit=args.limit)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    elif args.command == "summarise":
        try:
            df = load_csv(args.file)
            summarise(df, args.column)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    elif args.command == "sample":
        try:
            df = load_csv(args.file)
            sample(df, n=args.n, seed=args.seed)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    elif args.command == "missing":
        try:
            df = load_csv(args.file)
            missing(df, show_all=args.all)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    elif args.command == "filter":
        try:
            df = load_csv(args.file)
            result = filter_rows(df, args.column, args.value)
            print(f"Matched {len(result)} row(s).\n")
            print(result.head(args.limit).to_string(index=False))
            if args.output:
                result.to_csv(args.output, index=False)
                print(f"\nSaved to {args.output}")
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    elif args.command is None:
        parser.print_help()


if __name__ == "__main__":
    main()
