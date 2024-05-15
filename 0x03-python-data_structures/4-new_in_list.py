#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """### Replace a list element like in C

    Args:
        my_list (list): Array of elements
        idx (int): position of element
        element (str): String to replace at idx

    Returns:
        list: original list if error, modified list otherwise
    """
    if idx in range(len(my_list)):
        my_copy = my_list.copy()
        my_copy.remove(my_copy[idx])
        my_copy.insert(idx, element)
        return my_copy

    return my_list
