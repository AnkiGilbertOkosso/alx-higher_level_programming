#!/usr/bin/python3
"""A file-appending function."""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text file.
    Args:
        filename (str): A name of the file to append to.
        text (str): A string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as n:
        return n.write(text)
