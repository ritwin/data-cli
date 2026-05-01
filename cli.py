import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    print(f"Hi {args.name}")


if __name__ == "__main__":
    main()
