#!/usr/bin/python3

def best_score(a_dictionary):
    """ ### Find the student w the best grade

    ### Args:
        a_dictionary (_dict_): _Input dictionary_

    ### Returns:
        _string_: _Key with max integer or None_
    """
    if a_dictionary is not None:
        maxx = max(list(a_dictionary.values()))
        for key in a_dictionary:
            if a_dictionary.get(key) == maxx:
                return key
    return None
