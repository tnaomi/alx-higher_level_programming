#!/usr/bin/python3
""" Checks if obj inherits from a class """


def inherits_from(obj, a_class):
    """
    Returns `True` if `obj` inherits from `a_class`; else `False`
    """
    return isinstance(type(obj),
                      a_class) or type(obj) in a_class.__subclasses__()
