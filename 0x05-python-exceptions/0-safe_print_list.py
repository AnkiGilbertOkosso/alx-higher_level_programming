#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints xelements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements from my_list to print.

    Returns:
        The number of elements printed.
    """
    num_count = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            num_count += 1
        except IndexError:
            break
    print("")
    return (num_count)
