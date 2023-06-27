#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divides.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for n in range(0, list_length):
        try:
            divide = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            new_list.append(divide)
    return (new_list)
