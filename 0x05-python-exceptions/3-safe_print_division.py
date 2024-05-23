#!/usr/bin/python3

def safe_print_division(a, b):
    """ Divide two integers and display the result
    """
    try:
        mod = a / b
    except (ZeroDivisionError):
        mod = None
    finally:
        print("Inside result: {}".format(mod))
        return mod
