#!/usr/bin/python3

def element_at(my_list, idx):
    """### Find an element at a given index
    Args:
        my_list (_list_): _Input array of integers_
        idx (_int_): _Index of the list_

    Returns:
        list or None: list if idx w/in range and None if error
    """
    if idx in range(len(my_list)):
        return my_list[idx]
    return None
