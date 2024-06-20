#!/usr/bin/python3
""" Contains a class `MyList` """


class MyList(list):
    """ Defines `MyList` inherited from `list` """

    def print_sorted(self):
        """ Returns `list` object, sorted in ascending """
        print(sorted(self))
