#!/usr/bin/python3
"""this module define ibutes to objects"""


def add_attribute(obj, att, value):
    """Add a new attrib ssible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
