#!/usr/bin/python3
"""writiring"""
import math


class MagicClass:
    """seic"""

    def __init__(self, radius=0):
        """ wricstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """agaicstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """sucstring"""
        return 2 * math.pi * self.__radius
