#!/usr/bin/python3
"""Module with a lookup class"""


class BaseGeometry:
    """
        Inherits from list and provides a
        method to print sorted list.
    """
    def area(self):
        """Inherits from list and provides a"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Inherits from list and provides a"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        Inherits from list and provides a
        method to print sorted list.
    """
    def __init__(self, width, height):
        """Inherits from list and provides a"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
