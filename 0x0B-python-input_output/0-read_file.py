#!/usr/bin/python3
"""Text file-reading function."""


def read_file(filename=""):
    """Print contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as fn:
        print(fn.read(), end="")
