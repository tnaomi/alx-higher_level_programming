#!/usr/bin/python3
""" Print the letters of the alphabet without storing in a var """
for indx in range(97, (97+26)):
    print("{}".format(chr(indx)), end='')
