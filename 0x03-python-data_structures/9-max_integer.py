#!/usr/bin/python3
def max_integer(my_list=[]):
    """### Find the max integer of an input list

    #### Args:
        my_list (list): Input list. Assumed integers. Defaults to [].

    #### Returns:
        Int: max integer
    """
    length = len(my_list)

    if length == 0:
        return None

    stores = my_list.copy()
    stores.sort(reverse=True)

    return stores[0]
