#!/usr/bin/python3
""" Adds attribute to an object """


def add_attribute(cls, name, value):
    """ Add attr to an object if it has a __dict__ attr"""
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(cls, name, value)
