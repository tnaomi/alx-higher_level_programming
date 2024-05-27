#!/usr/bin/python3
"""Module

Defines a function for concatenating strings
"""


def say_my_name(first_name, last_name=""):
    """ Concatenates strings. Appropriate error handling

    Args:
        `first_name` (str)  : String
        `last_name` (str)   : Second string. Defaults to "".

    Raises:
        TypeError           : If `first_name` is not a valid string
        TypeError           : If `last_name` is not a valid string
    """
    my_name = "My name is"

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(" ".join([my_name, first_name, last_name]))
