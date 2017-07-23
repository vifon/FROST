#!/usr/bin/env python3
from os.path import getsize
import argparse
import sys

if sys.stdout.isatty():
    DATA_COLOR = "\033[32m"
    RESET_COLOR = "\033[0m"
else:
    DATA_COLOR = ""
    RESET_COLOR = ""

INDENT = 2


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('assets', nargs='+')
    parser.add_argument('--quiet', '-q', action='store_true')
    args = parser.parse_args()
    for asset in args.assets:
        print(asset)
        if not args.quiet and getsize(asset) > 0:
            print(DATA_COLOR, end="")
            with open(asset, 'r') as asset_fh:
                for line in asset_fh:
                    print(INDENT * " " + line, end="")
            print(RESET_COLOR, end="")


if __name__ == '__main__':
    main(sys.argv)
