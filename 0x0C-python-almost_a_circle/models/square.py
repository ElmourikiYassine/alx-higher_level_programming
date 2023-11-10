#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
            self.__width = value
            self.__height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x,
                self.y, self.__size)
