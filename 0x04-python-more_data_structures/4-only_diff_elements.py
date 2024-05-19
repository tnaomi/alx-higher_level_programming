#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """### Find the union of complement of sets
    i.e elements found in only one particular set
    ### Args:
        set_1 (_set_): First set
        set_2 (_set_): Second set

    ### Returns:
        _set_: an intersection of two sets
    """
    common = set(set_1.symmetric_difference(set_2))
    return common
