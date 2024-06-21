#!/usr/bin/python3
""" Contains function `read_file` """


def read_file(filename=""):
    """ Reads a file in `utf-8` and prints to `stdout` """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except Exception:
        pass
