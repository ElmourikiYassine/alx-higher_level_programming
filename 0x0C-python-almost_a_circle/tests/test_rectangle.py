#!/usr/bin/python3
"""Rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        r = Rectangle(10, 20, 5, 8, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.id, 1)

    def test_default_values(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_getters_and_setters(self):
        r = Rectangle(10, 20, 5, 8, 1)
        r.width = 15
        r.height = 25
        r.x = 3
        r.y = 6
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 6)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3, 7)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3, 7)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3, 7)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3, 7)

    def test_non_integer_width(self):
        with self.assertRaises(TypeError):
            Rectangle("5", 10, 2, 3, 7)

    def test_non_integer_height(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "10", 2, 3, 7)

    def test_non_integer_x(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "2", 3, 7)

    def test_non_integer_y(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "3", 7)

    def test_area(self):
        r = Rectangle(5, 10, 2, 3, 7)
        self.assertEqual(r.area(), 50)

    def test_area_after_resize(self):
        r = Rectangle(5, 10, 2, 3, 7)
        r.width = 3
        r.height = 7
        self.assertEqual(r.area(), 21)

if __name__ == '__main__':
    unittest.main()
