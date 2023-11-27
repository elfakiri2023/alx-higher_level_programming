#!/usr/bin/python3
"""A class"""

class Rectangle:
    """this repangle"""

    def __init__(self, width=0, height=0):
        """Initialigle class
        Args:
            width: represehe rectangle
            height: represents ectangle
        Raises:
            TypeError: if sizinteger
            ValueError: if size zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retriibute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setsribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrite"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets hbute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
