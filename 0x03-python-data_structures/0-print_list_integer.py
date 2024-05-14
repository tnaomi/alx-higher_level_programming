#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """### Print all integers of a list

    Args:
        my_list (list, optional): A list of integers. Defaults to [].
    """
    for el in my_list:
        print("{:d}".format(el))
