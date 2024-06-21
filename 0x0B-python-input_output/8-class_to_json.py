#!/usr/bin/python3
"""
Contains function `class_to_json(obj)`
"""


def class_to_json(obj):
    """ Returns a class' `__dict__` rep w a simple `JSON` structure """
    return obj.__dict__
