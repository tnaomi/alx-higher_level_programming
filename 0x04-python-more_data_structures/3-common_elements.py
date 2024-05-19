#!/usr/bin/python3

def common_elements(set_1, set_2):
    """### Return common elements in two sets

    ### Args:
        set_1 (_set_): First set
        set_2 (_set_): Second set

    ### Returns:
        _set_: an intersection of two sets
    """
    common = set(set_1.intersection(set_2))
    return common
