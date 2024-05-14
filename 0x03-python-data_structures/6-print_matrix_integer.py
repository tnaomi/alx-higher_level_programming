#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """### Print the elements of a list matrix

    Args:
        matrix (list, optional): Input matrix. Defaults to [[]].
    """
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" ")
