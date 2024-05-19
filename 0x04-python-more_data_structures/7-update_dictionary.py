#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """ Replace or add a key/value pair

    Args:
        a_dictionary (_dict_): _Input dictionary_
        key (_string_): dictionary key
        value (_any_): dictionary value

    Returns:
        _dict_: _An updated dictionary_
    """
    a_dictionary.update({key: value})
    return a_dictionary
