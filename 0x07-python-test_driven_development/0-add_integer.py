#!/usr/bin/python3
"""Module

`0-add_integer`:
Defines a function that adds two integers `a` and `b`.
"""


def add_integer(a, b=98):
    """ Adds two integers `a` and `b`

    Args:
        a (int): Can be `float`. Casted to `int`
        b (int, optional): Can be `float`. Casted to `int`. Defaults to 98.

    Raises:
        TypeError: if `a` or `b` is not `int` or `float`

    Returns:
        int: `a` + `b`
    """
    allwd_types = [int, float]
    if type(a) not in allwd_types:
        raise TypeError("a must be an integer")
    elif type(b) not in allwd_types:
        raise TypeError("b must be an integer")
    summ = int(a) + int(b)
    return summ
