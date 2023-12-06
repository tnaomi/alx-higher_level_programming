#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique=my_list.copy()

    for i in  unique:
        while unique.count(i)!=1:
            unique.remove(i)

    unique_sum=0
    for x in unique:
        unique_sum+=x
    return(unique_sum)
