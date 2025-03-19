#!/usr/bin/env python3
import sys
import antigravity


def main():
    """
    This is to call the antigravity module with the given arguments.
    https://github.com/python/cpython/blob/main/Lib/antigravity.py
    https://xkcd.com/426/
    """
    if len(sys.argv) != 4:
        print("Usage: python3 geohashing.py <date> <latitude> <longitude>")
        print(
            "Example: python3 geohashing.py 2005-05-26-10458.68 37.421542 -122.085589"
        )
        sys.exit(1)

    date_str = sys.argv[1]
    date_bytes = date_str.encode("utf-8")

    try:
        latitude = float(sys.argv[2])
        longitude = float(sys.argv[3])
    except ValueError:
        print("Please enter valid numbers for latitude and longitude.")
        sys.exit(1)

    try:
        antigravity.geohash(latitude, longitude, date_bytes)
    except Exception as e:
        print("Error while calculating geohash:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
