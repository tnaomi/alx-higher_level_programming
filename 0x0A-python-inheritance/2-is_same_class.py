#!/usr/bin/python3
""" Checks if obj is an instance of a class """


def is_same_class(obj, a_class):
    """
    Returns `True` if `obj` is an exact instance of `a_class`; else `False`
    """
    #
    """ `return isinstance(obj, class)`
    This always returns `True` bc almost all cls in Python are inherited
    """
    return type(obj) is a_class
