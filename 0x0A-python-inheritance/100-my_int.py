#!/usr/bin/python3
""" Contains a class `MyInt` """


class MyInt(int):
    """ Defines `MyInt` """

    def __init__(self, value):
        """ Initialises `MyInt` w `number` """
        if type(value) is not int:
            raise TypeError("value must be an integer")
        else:
            if value <= 0:
                raise ValueError("value must be greater than 0")
            else:
                self = value

    def __eq__(self, value: object) -> bool:
        """ Invert equality check """
        return super().__ne__(value)

    def __ne__(self, value: object) -> bool:
        """ Invert inequality check """
        return super().__eq__(value)
