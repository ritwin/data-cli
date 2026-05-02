from __future__ import annotations

import argparse
from ingest import load_csv, inspect, summarise


def main() -> None:
    parser = argparse.ArgumentParser(description="data-cli: explore CSVs from the command line")
    subparsers = parser.add_subparsers(dest="command")

    inspect_parser = subparsers.add_parser("inspect", help="Print basic info about a CSV")
    inspect_parser.add_argument("--file", required=True, help="Path to CSV file")

    summarise_parser = subparsers.add_parser("summarise", help="Summarise a specific column")
    summarise_parser.add_argument("--file", required=True)
    summarise_parser.add_argument("--column", required=True)

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

    elif args.command is None:
        parser.print_help()


if __name__ == "__main__":
    main()
