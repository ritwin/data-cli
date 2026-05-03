from __future__ import annotations

import argparse
from ingest import load_csv, inspect, summarise, missing, filter_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="data-cli: explore CSVs from the command line")
    subparsers = parser.add_subparsers(dest="command")

    inspect_parser = subparsers.add_parser("inspect", help="Print basic info about a CSV")
    inspect_parser.add_argument("--file", required=True, help="Path to CSV file")

    summarise_parser = subparsers.add_parser("summarise", help="Summarise a specific column")
    summarise_parser.add_argument("--file", required=True)
    summarise_parser.add_argument("--column", required=True)

    missing_parser = subparsers.add_parser("missing", help="Show columns with missing values")
    missing_parser.add_argument("--file", required=True)
    missing_parser.add_argument("--all", action="store_true", help="Show all columns, including complete ones")

    filter_parser = subparsers.add_parser("filter", help="Filter rows by column value")
    filter_parser.add_argument("--file", required=True)
    filter_parser.add_argument("--column", required=True)
    filter_parser.add_argument("--value", required=True)
    filter_parser.add_argument("--limit", type=int, default=10, help="Max rows to show (default: 10)")

    args = parser.parse_args()

    if args.command == "inspect":
        try:
            df = load_csv(args.file)
            inspect(df)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    elif args.command == "summarise":
        try:
            df = load_csv(args.file)
            summarise(df, args.column)
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
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

    elif args.command is None:
        parser.print_help()


if __name__ == "__main__":
    main()
