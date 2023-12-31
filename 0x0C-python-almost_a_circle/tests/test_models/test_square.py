#!/usr/bin/python3
"""Module for Square unittest"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Base Class"""

    def setUp(self):
        Base.__nb_objects = 0
        pass

    def test_class(self):
        """Test for Square Class"""
        self.assertEqual(str(
            Square), "<class 'models.square.Square'>")

    def test_inheritance(self):
        """Test inheritance Square->Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_constructor(self):
        """Test constructor"""
        with self.assertRaises(TypeError) as e:
            r = Square()

    def test_constructor_args(self):
        """Test constructor"""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 5, 8, 9)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"

        self.assertEqual(str(e.exception), s)


if __name__ == '__main__':
    unittest.main()
