#!/usr/bin/python3
"""
This module has one function
"""

def add_integer(a, b=98):
    """Return the sum of two integers

    Args:
        a: argument
        b: argument

    Returns:
        Sum

    Raises:
        TypeError
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
