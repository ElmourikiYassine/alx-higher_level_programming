#!/usr/bin/python3
"""Module with a lookup class"""


def inherits_from(obj, a_class):
    """
        Inherits from list and provides a
        method to print sorted list.
    """
    return False if type(obj) == a_class else isinstance(obj, a_class)
