#!/usr/bin/python3
""" Contains a class `Rectangle` """
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """ Defines `Rectangle` """
    def __init__(self, width, height):
        """ Initialises `Rectangle` w `width` and `height` """
        self.__width = BG.integer_validator(self, "width", width)
        self.__height = BG.integer_validator(self, "height", height)
