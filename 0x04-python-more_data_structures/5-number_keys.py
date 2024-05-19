#!/usr/bin/python3

def number_keys(a_dictionary):
    """### Return the number of keys in a dictionary

    ### Args:
        a_dictionary (_dict_): _Input dict_

    ### Returns:
        _int_: _Count of keys_
    """
    count = 0
    for key in a_dictionary:
        count += 1
    return count
