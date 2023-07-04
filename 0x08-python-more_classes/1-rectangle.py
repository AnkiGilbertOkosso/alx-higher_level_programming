#!/usr/bin/python3
"""a Rectangle class."""


class Rectangle:
    """a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializ a new Rectangle.
        Args:
            width (int): For the width of the new rectangle.
            height (int): For the height of the new rectangle.
        """
        self.width = width
        self.height = height

        @property
    def width(self):
        """Getting and setting width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting and setting height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
