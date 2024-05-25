#!/usr/bin/python3

class Square:
    """Square class. Initiate size w initial val. Handle errors

    Attributes:
        __size : Private attribute for defining a square
    """

    def __init__(self, size=0):
        """ Generate private attribute `size`.
        Error handling if not int or negative.

        Args:
            size (_int_): _Positive integer_
        """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
            pass
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
            pass
        else:
            self.__size = size
