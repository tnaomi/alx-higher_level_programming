#!/usr/bin/python3
def multiple_returns(sentence):
    """### Returns tuple w string length & first character

    #### Args:
        sentence (str): Input string
    """
    length = len(sentence)

    if length == 0:
        first = None
    else:
        first = sentence[0]
    return (length, first)
