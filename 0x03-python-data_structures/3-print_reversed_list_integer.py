#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """### Print a list of integers in reversed order

    #### Args:
        my_list (_list_, _optional_): An array of elements. Defaults to [].
    """
    if my_list is not None:
        for indx in range((len(my_list) - 1), -1, -1):
            print("{:d}".format(my_list[indx]))
