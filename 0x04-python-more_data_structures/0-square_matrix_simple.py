#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """### Compute the square value of all integers

    ### Args:
        matrix (__list__, optional): Input integer array. Defaults to __[]__.

    ### Returns:
        _list_: nested list of squares
    """
    results = [[x**2 for x in y] for y in matrix]
    return results
