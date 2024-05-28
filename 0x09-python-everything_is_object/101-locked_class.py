#!/usr/bin/python3
""" Module: Locked class"""


class LockedClass:
    """ Class without __dict__ and locked attributes """
    __slots__ = "first_name"
