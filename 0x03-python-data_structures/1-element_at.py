#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 | idx > len(my_list):
        return None
    for i in range(len(my_list)):
        while idx != i:
            i += 1
            pass
        return my_list[i]
