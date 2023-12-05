#!/usr/bin/python3
"""This moding function"""


def read_file(filename=""):
    """Prints the file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
