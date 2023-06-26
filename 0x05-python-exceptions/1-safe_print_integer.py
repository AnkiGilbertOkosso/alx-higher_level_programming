#!/usr/bin/python3

def safe_print_integer(value):
    """
     prints an integer with "{:d}".format().

     Agrs:
        value (ints): The integer to be printed.
    Returns:
        If a TypeError or ValueError occurs - False
        else - Ture
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
