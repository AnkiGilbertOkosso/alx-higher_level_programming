#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_number = number % 10
    else:
        last_number = number % -10
        last_number *= -1

    print("{:d}".format(last_number), end='')
    return (last_number)
