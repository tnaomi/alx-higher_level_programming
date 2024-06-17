#!/usr/bin/python3
""" Prints ALL NUMBERS from 0 to 99 in asceding order as 2 digits """
for number in range(0, 100):
    if (number != 99):
        print(f"{{:02d}}, ".format(number), end='')
    else:
        print(f"{{:02d}}".format(number))
