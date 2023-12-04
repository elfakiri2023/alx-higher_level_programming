#!/usr/bin/python3
"""DefineseGeometry"""


class BaseGeometry:
    """this claetry"""

    def area(self):
        """method nonted yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
