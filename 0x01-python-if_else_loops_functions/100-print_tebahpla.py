#!/usr/bin/python3
""" Print the letters of the alphabet in reverse, with alternate capitals """
for indx in range((97+25), 96, -1):
    if indx % 2 != 0:
        indx -= 32
    print("{}".format(chr(indx)), end='')
    if indx % 2 != 0:
        indx += 32
