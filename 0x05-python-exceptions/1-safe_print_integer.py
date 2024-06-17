#!/usr/bin/python3

def safe_print_integer(value):
    """ Print an integer with string format()
    """
    try:
        print("{:d}".format(value))
        status = True
    except ValueError:
        status = False
    return status
