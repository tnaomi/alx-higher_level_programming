#!/usr/bin/python3
""" Contains function `write_file` """


def write_file(filename="", text=""):
    """ Writes to a file in `utf-8` and returns char count """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
