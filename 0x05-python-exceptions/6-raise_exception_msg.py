#!/usr/bin/python3

def raise_exception_msg(message=""):
    """ Raise an exception with a message
    """
    if message is not None:
        raise NameError(message)
