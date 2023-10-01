#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    n = 0
    x = len(list_of_integers)
    y = ((x - n) // 2) + n
    y = int(y)
    if x == 1:
        return list_of_integers[0]
    if x == 2:
        return max(list_of_integers)
    if list_of_integers[y] >= list_of_integers[y - 1] and\
            list_of_integers[y] >= list_of_integers[y + 1]:
        return list_of_integers[y]
    if y > 0 and list_of_integers[y] < list_of_integers[y + 1]:
        return find_peak(list_of_integers[y:])
    if y > 0 and list_of_integers[y] < list_of_integers[y - 1]:
        return find_peak(list_of_integers[:y])
