#!/usr/bin/python3
def remove_char_at(str, n):
    old_str = 0
    string = ""
    for j in str:
        if old_str != n:
            string += j
        old_str += 1
    return string
