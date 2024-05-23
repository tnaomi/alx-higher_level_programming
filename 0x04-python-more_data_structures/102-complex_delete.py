#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """ ### Returns a copy of __my_list__ with the multiple of number

    ### Args:
        my_list (_list_): _Input list_. Defaults to an empty list

    ### Returns:
        _list_: _A copy of the original list with vals multiplied_
    """
    list_copy = my_list.copy()
    results = map(lambda el: el * number, list_copy)
    return list(results)
