#!/usr/bin/python3
"""Create a Class Square"""


class Square:
    """This is a Class Square"""

    def __init__(self, size=0):
        """Stating a Square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """Getting the area of the Square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter of private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for size attribute private"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
