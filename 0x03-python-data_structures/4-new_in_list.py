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
    list_copy = my_list.copy()
    if idx < 0 | idx > len(list_copy):
        return list_copy

    for i in range(len(list_copy)):
        while idx != i:
            i += 1
            pass
        list_copy.remove(list_copy[idx])
        list_copy.insert((idx), element)
        return list_copy
