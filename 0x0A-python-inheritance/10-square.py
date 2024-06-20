#!/usr/bin/python3
""" Contains a class `Square` """
Rec = __import__('9-rectangle').Rectangle


class Square(Rec):
    """ Defines `Square` """
    def __init__(self, size):
        """ Initialises `Square` w `size` """
        self.__size = Rec.integer_validator(self, "size", size)

    def area(self):
        """ Implements the `area` """
        return self.__size ** 2
