#!/usr/bin/python3
"""this module de t inherits from int"""


class MyInt(int):
    """Invert i == and !="""

    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
