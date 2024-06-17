#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """ Delete a dict entry if key in dict otherwise,
    return an unchanged dictionary

    Args:
        a_dictionary (_dict_): _Input dictionary_
        key (_string_): dictionary key

    Returns:
        _dict_: _A modified dictionary_
    """
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
