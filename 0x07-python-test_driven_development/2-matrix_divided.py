#!/usr/bin/python3
"""
Module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): Matrix of integers/floats.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists,
                   if matrix or div is empty,
                   if one element of the matrix is not an integer or float,
                   if div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
        ValueError: If matrix or div is empty.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not div or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not matrix or not isinstance(matrix, list)\
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix should contain only integers or floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("each row of the matrix must have the same size")
    return [[round(num / div, 2) for num in row] for row in matrix]
