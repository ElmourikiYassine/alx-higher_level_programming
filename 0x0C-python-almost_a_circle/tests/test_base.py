#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_increment(self):
        """Test that the id is incremented properly."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_specific_id(self):
        """Test if the id is assigned properly when provided."""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_mixed_ids(self):
        """Test if id is incremented for objects with and without specific id."""
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 4)

if __name__ == '__main__':
    unittest.main()