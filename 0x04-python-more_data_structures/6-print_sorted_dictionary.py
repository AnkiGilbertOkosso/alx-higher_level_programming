#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    data = list(a_dictionary.keys())

    data.sort()
    for n in data:
        print("{}: {}".format(n, a_dictionary.get(n)))
