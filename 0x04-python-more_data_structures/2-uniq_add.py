#!/usr/bin/python3

def uniq_add(my_list=[]):
    """### Adds all unique integers

    ### Args:
        my_list (__list__, optional): _Input array_. Defaults to __[]__.
    """
    uniq = []
    for num in my_list:
        if num in uniq:
            continue
        uniq.append(num)
    return sum(uniq)
