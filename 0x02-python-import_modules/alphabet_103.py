#!/usr/bin/python3

def print_uppercase():
    """### Print all the letters of the alphabet as uppercase
    """
    for indx in range(97, (97+26)):
        print("{}".format(chr(indx)).upper(), end='')
    print("")
