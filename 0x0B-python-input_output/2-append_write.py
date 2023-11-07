#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and\n
    returns the number of characters added.
    Creates the file if it doesn't exist.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
