#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Print `x` elements of a list
    """
    i = 0
    if my_list is None or x == 0:
        print()
        return actual
    try:
        for i in range(x):
            print(my_list[i], end='')
    except Exception:
        i -= 1
    finally:
        print()
        return i + 1
