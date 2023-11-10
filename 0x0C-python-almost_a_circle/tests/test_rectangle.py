#!/usr/bin/python3
"""Rectangle module"""
import sys
import unittest
from io import StringIO
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

    def test_display(self):
        r = Rectangle(3, 2, 1, 1, 1)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '###\n###\n')

    def test_display_no_offset(self):
        r = Rectangle(2, 2, 0, 0, 1)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '##\n##\n')

    def test_str(self):
        r = Rectangle(3, 2, 1, 1, 1)
        expected_output = "[Rectangle] (1) 1/1 - 3/2"
        self.assertEqual(str(r), expected_output)

    def test_display(self):
        r = Rectangle(3, 2, 1, 1, 1)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '\n ###\n ###\n')

    def test_update_0(self):
        r = Rectangle(3, 2, 1, 1, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test2_update_0(self):
        r = Rectangle(3, 2, 1, 1, 1)
        r.update(89, 2, 3)
        self.assertEqual((r.id, r.width, r.height), (89, 2, 3))

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

if __name__ == '__main__':
    unittest.main()
