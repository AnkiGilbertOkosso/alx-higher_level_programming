#!/usr/bin/python3
"""A script that:
- authenticates using your GitHub credentials (username and password)
- makes a request to the GitHub API to retrieve and
- display your user ID
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    respon = requests.get("https://api.github.com/user", auth=auth)
    print(respon.json().get("id"))
