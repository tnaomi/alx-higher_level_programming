#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ Print the first `x` elements of a list and only integers
    """
    if my_list is None or x == 0:
        print()
        return 0
    count = 0
    for indx in range(x):
        try:
            print("{:d}".format(my_list[indx]), end='')
        except (ValueError, TypeError):
            pass
        else:
            count += 1
    print()
    return count
