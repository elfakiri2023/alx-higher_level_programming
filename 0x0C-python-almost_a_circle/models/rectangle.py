#!/usr/bin/python3
""" Module that defines a Rectangle Class """
from models.base import Base


class Rectangle(Base):

    """
    Class that inherits from Base
    Attributes: __width, __height, __x, __y.
    Methods: __init__ (self, width, height, x=0, y=0, id=None).
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing our data attributes """
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

    @property
    def width(self):
        """ Module that defines the Class for Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Module that defines a Rectangle Class """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Module that defines a Rectangle Class """
        return self.__height

    @height.setter
    def height(self, value):
        """ Module that defines a Rectangle Class """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Module that defines a Rectangle Class """
        return self.__x

    @x.setter
    def x(self, value):
        """ Module that defines a Rectangle Class """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Module that defines a Rectangle Class """
        return self.__y

    @y.setter
    def y(self, value):
        """ Module that defines a Rectangle Class """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Module that defines a Rectangle Class """
        return self.__width * self.__height

    def display(self):
        """ Module that defines a Rectangle Class """
        for j in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            print(self.__x * " " + "#" * self.__width)

    def __str__(self):
        """ Module that defines a Rectangle Class """
        return (
                "[Rectangle] ({}) {}/{} - {}/{}").format(
                    self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Module that defines a Rectangle Class """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Module that defines a Rectangle Class """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
