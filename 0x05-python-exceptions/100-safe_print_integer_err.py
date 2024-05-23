#!/usr/bin/python3

def safe_print_integer_err(value):
    """ Print error in stderr

    Args:
        value(_any_) : Variable to be printed,
                    if error, catch

    Returns:
        _bool__ : True if no print error, False otherwise
    """
    from sys import stderr

    try:
        print("{:d}".format(value))
    except ValueError as VE:
        print("Exception: {}".format(VE), file=stderr)
        status = False
    else:
        status = True
    return status
