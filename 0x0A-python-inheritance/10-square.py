#!/usr/bin/python3
"""Defi Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprare"""

    def __init__(self, size):
        """Iniare
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
