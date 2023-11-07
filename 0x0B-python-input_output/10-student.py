#!/usr/bin/python3
"""A class Student that defines a
   student by: (based on 9-student.py)
"""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings,
        only attributes in this list are retrieved.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for
                attr in attrs if hasattr(self, attr)}
