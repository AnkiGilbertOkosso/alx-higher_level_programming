#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a GET request to the URL
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    target_url = sys.argv[1]

    response = requests.get(target_url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
