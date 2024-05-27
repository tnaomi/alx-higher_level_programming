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

    elif len(text) == 0:
        return None

    cursor = 0

    for i in range(len(text)):
        if text[i] in operators:
            p.append(text[cursor: i + 1] + "\n\n")
            cursor = i + 1

    p.append(text[cursor:i + 1])

    p = [i.strip(' ') for i in p]

    print("".join(p), end='')
