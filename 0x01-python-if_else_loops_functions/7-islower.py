#!/usr/bin/python3
""" Checks for lowercase characters """


def islower(c):
    """# Check if c is lowercase.
    #### Don't  use `str.upper` or `str.isupper`
    """
    if ord(c) not in range(97, 97+26):
        return False
    else:
        return True
