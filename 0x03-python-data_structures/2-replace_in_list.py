#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """### Replace a list element like in C

    Args:
        my_list (list): Array of elements
        idx (int): position of element
        element (str): String to replace at idx

    Returns:
        list: original list if error, modified list otherwise
    """
    if idx < 0 | idx > len(my_list):
        return my_list
    for i in range(len(my_list)):
        while idx != i:
            i += 1
            pass
        my_list.remove(my_list[idx])
        my_list.insert((idx), element)
        return my_list
