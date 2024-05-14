#!/usr/bin/python3
def multiple_returns(sentence):
    """### Returns tuple w string length & first character

    #### Args:
        sentence (str): Input string
    """
    length = len(sentence)
    first = sentence[0]

    if length == 0:
        first = None

    return (length, first)
