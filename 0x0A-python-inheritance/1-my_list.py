#!/usr/bin/python3
"""Module with a lookup class"""


class MyList(list):
    """
        Inherits from list and provides a
        method to print sorted list.
    """
    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
