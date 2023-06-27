#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result.

    Args:
        a (int): First Integer
        b (int): Second integer
    Returns:
         the value of the division, otherwise: None
    """
    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
