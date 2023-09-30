#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    da = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, da)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
