#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: Resulting matrix.

    Raises:
        ValueError: If m_a or m_b is not a list of lists,
                   if m_a or m_b is empty,
                   if one element of those list of lists is not an integer or float,
                   if m_a and m_b can't be multiplied.
        ValueError: If m_a or m_b is not a rectangle (all rows should be of the same size).
    """
    if not m_a or not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not m_b or not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a[0] or not m_a[0]:
        raise ValueError("m_a can't be empty")

    if not m_b[0] or not m_b[0]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    np_a = np.array(m_a)
    np_b = np.array(m_b)
    result = np.dot(np_a, np_b)

    return result
