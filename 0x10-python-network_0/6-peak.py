#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(lst):
    """Finds a peak in lst"""

    if lst is None or lst == []:
        return None
    low = 0
    high = len(lst)
    mid = ((high - low) // 2) + low
    mid = int(mid)
    if high == 1:
        return lst[0]
    if high == 2:
        return max(lst)
    if lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]:
        return lst[mid]
    if mid > 0 and lst[mid] < lst[mid + 1]:
        return find_peak(lst[mid:])
    if mid > 0 and lst[mid] < lst[mid - 1]:
        return find_peak(lst[:mid])
