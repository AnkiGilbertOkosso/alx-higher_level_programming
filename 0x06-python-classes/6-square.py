#!/usr/bin/python3
"""
Create a Class Square with:
- size and position private proprety
- method of area and method of print_square
- getters & setters.
"""


class Square:
    """For Class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """This is a Square with the size and position"""
        self.size = size
        self.postion = position

    def area(self):
        """getting the area of the Square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print a Square"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.postion[1]):
                print()
            for n in range(self.__size):
                print(" " * self.postion[0], end='')
                print("#" * self.__size)

    @property
    def size(self):
        """Getter of a private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for a size private attribute"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    @property
    def position(self):
        """Getter of Position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter of position"""
        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
