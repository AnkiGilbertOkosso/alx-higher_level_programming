#!/usr/bin/python3
"""JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """To Write object to the text file using JSON representation."""
    with open(filename, "w") as n:
        json.dump(my_obj, n)
