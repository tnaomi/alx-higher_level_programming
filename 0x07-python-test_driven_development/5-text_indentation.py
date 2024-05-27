#!/usr/bin/python3
"""Module

5-text_indentation : contains `text_indentation(text)`
"""


def text_indentation(text):
    """ Prints `text` and inserts 2 indents at `.`,`?` and `:`

    Args:
        `text` (str): Input string

    Raises:
        TypeError: if `text` is not a valid string
    """
    p, operators = [], ['.', '?', ':']
    if type(text) is not str:
        del (p, operators)
        raise TypeError("text must be a string")

    p = [i for i in text]

    for i in range(len(p)):
        if p[i] in operators:
            p[i + 1] = "\n\n"

    print("".join(p), end='')
