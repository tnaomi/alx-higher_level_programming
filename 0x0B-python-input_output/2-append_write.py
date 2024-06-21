#!/usr/bin/python3
""" Contains function `append_write` """


def append_write(filename="", text=""):
    """ Creates, Appends to a file in `utf-8` and returns char count """
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
