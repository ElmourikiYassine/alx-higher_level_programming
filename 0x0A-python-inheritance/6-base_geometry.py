#!/usr/bin/python3
"""Module with a lookup class"""


class BaseGeometry():
    """
        Inherits from list and provides a
        method to print sorted list.
    """
    def area(self):
        raise Exception("area() is not implemented")
