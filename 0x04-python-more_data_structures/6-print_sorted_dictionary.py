#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys

    Args:
        a_dictionary (_dict_): _Input dictionary_

    Returns:
        _dict_: _A dictionary with ordered keys_
    """
    copy_dict = {}
    keys = list(a_dictionary.keys())
    keys.sort()
    copy_dict = {key: a_dictionary.get(key) for key in keys}
    print(copy_dict)
    return copy_dict
