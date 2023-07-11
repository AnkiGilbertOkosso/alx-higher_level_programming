#!/usr/bin/python3
"""A file-writing function."""


def write_file(filename="", text=""):
    """
    Write a string to a UTF8 text file.
    Args:
        filename (str): Name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as n:
        return n.write(text)