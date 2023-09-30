#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a req to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    re = requests.get(url)
    print(re.headers.get("X-Request-Id"))
