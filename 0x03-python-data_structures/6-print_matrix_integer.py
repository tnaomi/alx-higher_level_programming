#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """### Print the elements of a list matrix

    Args:
        matrix (list, optional): Input matrix. Defaults to [[]].
    """
    for row in matrix:
        space = ""
        for column in row:
            print("{:s}{:d}".format(space, column), end="")
            space = " "
        print()
