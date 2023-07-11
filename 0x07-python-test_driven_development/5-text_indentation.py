#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    num = 0
    while num < len(text) and text[num] == ' ':
        num += 1

    while num < len(text):
        print(text[num], end="")
        if text[num] == "\n" or text[num] in ".?:":
            if text[num] in ".?:":
                print("\n")
            num += 1
            while num < len(text) and text[num] == ' ':
                num += 1
            continue
        num += 1
