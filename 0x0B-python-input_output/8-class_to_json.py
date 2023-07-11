#!/usr/bin/python3
"""Python class-to-JSON function."""


def class_to_json(obj):
    """To Return dictionary represntation of a simple data structure."""
    return obj.__dict__
