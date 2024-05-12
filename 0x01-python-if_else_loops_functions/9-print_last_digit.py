#!/usr/bin/python3
"""Print the mod of a number w/out newline"""


def print_last_digit(number):
    """ # Print last digit of a number
    """
    def _mod(number, base):
        """#### Accounts for the behaviour of Python on a negative number """
        mod = number % base
        return mod if not mod else mod - base if number < 0 else mod

    mod = _mod(number, 10)
    if mod < 0:
        mod *= -1
    print(mod, end='')
    return (mod)
