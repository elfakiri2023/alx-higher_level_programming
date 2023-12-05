#!/usr/bin/python3
"""This modulnction."""


def append_write(filename="", text=""):
    """Appends text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
