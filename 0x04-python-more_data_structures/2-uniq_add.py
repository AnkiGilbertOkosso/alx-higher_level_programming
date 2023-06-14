#!/usr/bin/python3

def uniq_add(my_list=[]):
    lists = set(my_list)
    num = 0

    for n in lists:
        num += n

    return (num)
