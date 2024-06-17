#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """ Multiply by 2 all the values

    Args:
        a_dictionary (_dict_): _Input dictionary_

    Returns:
        _dict_: _A modified dictionary_
    """

    for key in a_dictionary:
        a_dictionary[key] = a_dictionary.get(key) * 2
    return a_dictionary
