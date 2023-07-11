#!/usr/bin/python3
"""JSON file-reading function."""
import json


def load_from_json_file(filename):
    """To Create Python object from a JSON file."""
    with open(filename) as n:
        return json.load(n)
