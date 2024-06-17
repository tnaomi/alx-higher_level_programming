#!/usr/bin/python3

def safe_function(fct, *args):
    """ __Execute a function safely__

    Args:
        fct (_ptr_): _a pointer to a function_

    Returns:
        _any_: _result of the function or None_
    """
    from sys import stderr

    if fct is not None:
        try:
            result = fct(*args)
        except Exception as X:
            print("Exception: {}".format(X), file=stderr)
            result = None
    return result
