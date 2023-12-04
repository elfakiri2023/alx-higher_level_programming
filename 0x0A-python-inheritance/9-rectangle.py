#!/usr/bin/python3
"""Defines  BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class reGeometry"""

    def __init__(self, width, height):
        """Intializngle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns ectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the prn of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
