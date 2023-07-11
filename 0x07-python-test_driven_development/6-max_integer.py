#!/usr/bin/python3
"""A Module to find the max integer in a list
"""


def max_integer(list=[]):
    """A Function to the find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    sol = list[0]
    n = 1
    while n < len(list):
        if list[n] > sol:
            sol = list[n]
        n += 1
    return sol
