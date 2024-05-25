#!/usr/bin/python3

"""Based on `4-square.py`, methods for comparison
"""


class Square:
    """Square class.
    - Initiate private attribute `size`

    Attributes:
        __size  : Size of the square; Private attr; positive integer only

    Methods:
        `size(self)`        : to retrieve __size
        `size(self, value)` : to set __size
        `area(self)`        : to return square area (public instance method)
    """

    def __init__(self, size=0):
        """ Generate private attribute `size`.

        Args:
            size (_int_): Positive integer
        """
        self.__size = size

    def __eq__(self, value):
        """ Compares two objects and returns `bool`"""
        return self.area() == value.area()

    def __le__(self, value):
        """ Compares two objects less than or equal to
        """
        return self.area() <= value.area()

    def __ge__(self, value):
        """ Compares two objects greater than or equal to
        """
        return self.area() >= value.area()

    def __ne__(self, value):
        """ Compare two objects for inequality"""
        return self.area() != value.area()

    def __lt__(self, value):
        """ Compares two objects for min """
        return self.area() < value.area()

    def __gt__(self, value):
        """ Compares two objects for max """
        return self.area() > value.area()

    @property
    def size(self):
        """Get `__size` as property. GETTER

        Returns:
            _int_: _size of the square_
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set or Update `__size` w new `value`.
        Appropriate error handling. SETTER

        Args:
            value (_type_): _description_

        Raises:
            ValueError: _if value is less than 0 i.e. negative_
            TypeError: _if value is not an integer_
        """
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        """ Generate public class attribute `area``
        """
        return self.__size**2
