#!/usr/bin/python3
"""
    This is a unittest file for class Base
"""
import unittest
import inspect
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Test cases"""
    def setUp(self):
        Base.__nb_objects = 0
        pass
        
    def test_base_is_class(self):
        # Check if Base is a class
        self.assertTrue(inspect.isclass(Base))

    def test_base_is_not_none(self):
        # Check if Base instance is not None
        b = Base()
        self.assertIsNotNone(b)

    def test_base_is_instance(self):
        # Check if Base instance is an instance of Base class
        b = Base()
        self.assertTrue(isinstance(b, Base))

    def test_base_is_type(self):
        # Check if Base instance is of type Base
        b = Base()
        self.assertTrue(type(b) is Base)

    def test_create_instance_without_passing_id(self):
        # Check if instance of Base is created without passing id
        obj_b = Base()
        self.assertIsNotNone(obj_b.id)

    def test_create_instance_with_passing_id(self):
        # Check if instance of Base is created with passing id
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_create_instance_without_id(self):
        # Check if multiple instances of Base have different ids
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_create_instance_incremental_id(self):
        # Check if ids of multiple instances of Base are incremental
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

    def test_create_instance_nb_objects(self):
        # Check if id of instance of Base is equal to __nb_objects
        obj_id = Base()
        self.assertEqual(obj_id.id, Base._Base__nb_objects)

    def test_D_constructor(self):
        # Check constructor signature without passing self
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        # Check constructor signature with 2 not self args
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_to_json_string(self):
        # Check to_json_string() method
        with self.assertRaises(TypeError) as ex:
            Base.to_json_string()
        msg = "to_json_string() missing 1 required positional argument: 'list_dictionaries'"
        self.assertEqual(str(ex.exception), msg)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        data = [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}]
        self.assertEqual(len(Base.to_json_string(data)), len(str(data)))

        data = [{"testtest": 989898}]
        self.assertEqual(Base.to_json_string(data), '[{"testtest": 989898}]')

        data = [{}]
        self.assertEqual(Base.to_json_string(data), '[{}]')

        r = Rectangle(1, 2, 3, 4)
        dic = r.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(1, 2)
        r3 = Rectangle(2, 4, 6)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(), r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    def test_from_json_string(self):
        # Check from_json_string method
        with self.assertRaises(TypeError) as ex:
            Base.from_json_string()
        msg = "from_json_string() missing 1 required positional argument: 'json_string'"
        self.assertEqual(str(ex.exception), msg)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x":1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]

        self.assertEqual(Base.from_json_string(s), d)

        s = '[{}, {}]'
        d = [{}, {}]

        self.assertEqual(Base.from_json_string(s), d)

    def test_save_to_file(self):
        # Check save_to_file method
        d = [{'id': 4, 'width': 3, 'height': 5, 'x': 1, 'y': 2}]
        r = Rectangle(3, 5, 1, 2, 4)
        Rectangle.save_to_file([r])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(str(d).replace("'", '"'), file.read())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        d = [{'id': 1, 'size': 2, 'x': 5, 'y': 0}]
        sq = Square(2, 5, 0, 1)

        Square.save_to_file([sq])

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), str(d).replace("'", '"'))

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        
    def test_create(self):
        # Check create method
        r1 = Rectangle(5, 8, 2)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
    
    def test_load_from_file(self):
        # Check load_from_file method
        r1 = Rectangle(8, 10, 20, 50)
        r2 = Rectangle(66, 78)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(60)
        s2 = Square(73, 88, 47)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

if __name__ == "__main__":
    unittest.main()
