#!/usr/bin/python3

""" 
This module defines the Square class, which is a subclass of Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ 
        Getter method for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """ 
        Setter method for the size attribute.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ 
        Returns a string representation of the Square object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ 
        Updates the attributes of the Square object.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ 
        Returns a dictionary representation of the Square object.
        """
        return {
            'id': self.id, 'size': self.width,
            'x': self.x, 'y': self.y}
