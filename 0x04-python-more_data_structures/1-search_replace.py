#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """### Replace all occurences of an element in a list

    ### Args:
        my_list (__list__): input array
        search (_type_): element to search for
        replace (_type_): element to replace with

    ### Returns:
        _list_: modified copy of original list
    """
    modified = [el if el != search else replace for el in my_list]
    return modified
