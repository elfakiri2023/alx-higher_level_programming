#!/usr/bin/python3
"""
Size defaults to 0. Raise errors on invalid inputs.
"""


class Square:
    """A class that de"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
