#!/usr/bin/python3

"""Square class with methods.
NEW: Initialise private instance attribute `__size`
"""


class Square:
    """Square class. Initiate size

    Attributes:
        __size : Private attribute for defining a square
    """

    def __init__(self, size):
        """ Generate private attribute `size`

        Args:
            size (_type_): _Any value, no verification needed_
        """
        self.__size = size
