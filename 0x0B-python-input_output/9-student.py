#!/usr/bin/python3
"""This modudent"""


class Student:
    """Repredent."""

    def __init__(self, first_name, last_name, age):
        """Initudent
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dicthe Student"""
        return self.__dict__
