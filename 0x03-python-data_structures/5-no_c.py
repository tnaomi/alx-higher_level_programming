#!/usr/bin/python3

def no_c(my_string):
    """### Removes c and C from a string

    Args:
        my_string (str, optional): Input string. Defaults to NULL.
    """
    store = []
    for char in str(my_string):
        if char == 'c' or char == 'C':
            continue
        store.append(char)
    return "".join(store)
