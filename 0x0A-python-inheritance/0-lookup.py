#!/usr/bin/python3
"""Module with a lookup class"""


def lookup(obj):
    """
        A function that returns the list of available
        attributes and methods of an object:
        Attributes:
            object : object
    """
    return dir(obj)
