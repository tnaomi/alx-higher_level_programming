#!/usr/bin/python3

""" Square class with methods.
NEW: Add coordinates
"""


class Square:
    """Square class.
    - Initiate private attribute `size`
    - Initiate private attribute `position`

    Attributes:
        __size      : Size of the square; Private attr; positive integer only
        __position  : Pos. coordinates; Private attr; positive integer only

    Methods:
        `size(self)`        : to retrieve __size
        `size(self, value)` : to set __size
        `area(self)`        : to return square area (public instance method)
        `my_print(self)`    : print # as square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Generate private attribute `size`.

        Args:
            size (_int_): Positive integer
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get `__size` as property. GETTER

        Returns:
            _int_: _size of the square_
        """
        return self.__size

    @property
    def position(self):
        """ Get `__position` as property. GETTER

        Returns:
            _int_: _current position_
        """
        return self.__position

    @size.setter
    def size(self, value):
        """ Set or Update `__size` w new `value`.
        Appropriate error handling. SETTER

        Args:
            value (_int_): _new size value_

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

    @position.setter
    def position(self, value):
        """ Set or Update `__size` w new `value`.
        Appropriate error handling. SETTER

        Args:
            value (_int_): _position_

        Raises:
            ValueError: _if value is less than 0_
            TypeError: _if value is not integer tuple_
        """
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Generate public class attribute `area``
        """
        return self.__size**2

    def my_print(self):
        """ Print # as square. If 0, print empty line
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for k in range(self.size):
                print("{}{}".format(' '*self.__position[0], '#'*self.__size))
