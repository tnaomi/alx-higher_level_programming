#!/usr/bin/python3
""" Prints possible combinations from 0 to 99 in asceding order as 2 digits """
for number in range(0, 9):
    for suffix in range(1, 10):
        if suffix > number:
            if number != 8:
                print("{}{}".format(number, suffix), end=', ')
            else:
                print("{}{}".format(number, suffix))
