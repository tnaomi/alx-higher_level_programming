#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copy_list=list(my_list)
    for i in range(0, len(copy_list)):
        if copy_list[i]==search:
            copy_list.pop(i)
            copy_list.insert(i, replace)
    return copy_list
