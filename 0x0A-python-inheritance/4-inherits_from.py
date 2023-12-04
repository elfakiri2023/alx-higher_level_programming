#!/usr/bin/python3
"""checks if object
inherited from
"""


def inherits_from(obj, a_class):
    """Returns true if object is an i
    (directly or indirectl
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
