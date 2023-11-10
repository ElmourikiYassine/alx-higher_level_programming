#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_id_increment(self):
        """Test that the id is incremented properly."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 6)

    def test_specific_id(self):
        """Test if the id is assigned properly when provided."""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_mixed_ids(self):
        """Test if id is incremented for objects with and without specific id."""
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        self.assertEqual(b1.id, 7)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 8)

    def test_to_json(self):
        """Test if id is incremented for objects with and without specific id."""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, "[{\"x\": 2, \"y\": 8, \"id\": 9, \"height\": 7, \"width\": 10}]")

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        s1 = Square(2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        self.assertIsInstance(s2, Square)
        self.assertIsNot(s1, s2)

    def test_create_invalid_instance(self):
        invalid_instance = Base.create()
        self.assertIsNone(invalid_instance)

if __name__ == '__main__':
    unittest.main()
