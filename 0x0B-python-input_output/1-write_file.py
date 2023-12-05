#!/usr/bin/python3
"""This modug function."""


def write_file(filename="", text=""):
    """Writet file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
