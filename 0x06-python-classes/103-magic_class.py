#!/usr/bin/python3
""" MAGIC CLASS
Defines the MagicClass class and its modules
"""

from math import pi


class MagicClass:
    """ Magic class for a circle object

    Attributes:
        radius          : Protected instance attribute

    Methods:
        `area(self)`    : Returns area of the circle object
        `circum(self)`  : Returns circumference of the circle object
    """
    def __init__(self, radius=0):
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        elif radius < 0:
            raise ValueError("Radius must be positive")
        else:
            self.__radius = radius

    def area(self):
        """ Calculate circle object area

        Returns:
            int / float : circle area
        """
        return pi*(self.__radius**2)

    def circumference(self):
        """Calculate circumference of the circle object
        """
        return 2 * pi * self.__radius
