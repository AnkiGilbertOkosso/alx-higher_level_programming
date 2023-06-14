#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    direct = a_dictionary.copy()
    data = list(direct.keys())

    for n in data:
        direct[n] *= 2

    return (direct)
