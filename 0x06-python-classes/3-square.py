#!/usr/bin/python3

class Square:
    """Square class.
    - Initiate private attribute `size`
    - Initiate public attribute `area`

    Attributes:
        __size  : Size of the square; Private attr; positive integer only
        area    : Square area; Public attr; Positive integer
    """

    def __init__(self, size=0):
        """ Generate private attribute `size`.
        Error handling if not int or negative.

        Args:
            size (_int_): Positive integer
        """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
            pass
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
            pass
        else:
            self.__size = size

    def area(self):
        """ Generate public class attribute `area``
        """
        return self.__size**2
