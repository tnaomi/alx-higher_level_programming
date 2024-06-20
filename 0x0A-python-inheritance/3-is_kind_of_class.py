#!/usr/bin/python3
""" Checks if obj is an instance of a class (also inherited) """


def is_kind_of_class(obj, a_class):
    """
    Returns `True` if `obj` is an instance of `a_class`; else `False`
    """
    return isinstance(obj, a_class)
