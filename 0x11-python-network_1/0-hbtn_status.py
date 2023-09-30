#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as re:
        cont = re.read()
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode('utf-8')))
