import argparse
import sys


def main():
    """Console script for data_sdk."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into " "data_sdk.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma:no cover11441
