#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """### Delete an item at a given index
    If error, return the original list.
    Modify the existing list. Similar to pop()

    Args:
        my_list (list, optional): Input array of integers. Defaults to [].
        idx (int, optional): index. Defaults to 0.

    Returns:
        _type_: _description_
    """
    if idx in range(len(my_list)):
        my_list.remove(my_list[idx])
    return my_list
