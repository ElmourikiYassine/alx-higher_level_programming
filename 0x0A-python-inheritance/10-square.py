#!/usr/bin/python3
"""Module with a lookup class"""


class BaseGeometry:
    """
        Provides a method to calculate area
        and integer validation.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        Represents a rectangle and inherits
        from BaseGeometry class.
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
        Represents a square and inherits
        from Rectangle class.
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
