#!/usr/bin/python3
"""Module

`2-matrix_divided`:
Divides a matrix of lists by a scalar
"""


def matrix_divided(matrix, div):
    """ Divide a matrix of lists by a scalar

    Args:
        `matrix` (list): a matrix of lists
        `div` (int, float): scalar dividant

    Raises:
        TypeError: If `matrix` is not made of equal vectors
        TypeError: If `matrix` is not made of `int` or `float` lists
        TypeError: If `div` is not a number
        ZeroDivisionError: If `div` is zero

    Returns:
        list: Modified copy of `matrix`
    """

    allwd, allwd_types, result = True, [int, float], []
    uneq = "Each row of the matrix must have the same size"
    unallwd = "matrix must be a matrix (list of lists) of integers/floats"
    zero = "division by zero"
    no = "div must be a number"

    if matrix is None:
        return 0
    elif len(matrix) == 0 or (len(matrix) == 1 and len(matrix[0]) == 0):
        return 0
    cp = matrix.copy()

    if not all(len(i) == len(cp[0]) for i in cp):
        raise TypeError(uneq)

    for i in range(len(cp)):
        for j in range(len(cp[i])):
            if type(cp[i][j]) not in allwd_types:
                allwd = False
                break

    if allwd is False:
        raise TypeError(unallwd)
    elif type(div) not in allwd_types:
        raise TypeError(no)
    elif div == 0:
        raise ZeroDivisionError(zero)

    for i in cp:
        # preserves list formats than extend()
        result.append(list(round((j / div), 2) for j in i))

    return result
