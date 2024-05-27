#!/usr/bin/python3
"""Module

Contains a function `print_square`
"""


def print_square(size):
    """ Print a square with `#` of size `size`

    Args:
        size (int): Square length

    Raises:
        TypeError: If `size` is not an integer
        ValueError: If `size` is less than `0`
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
