#!/usr/bin/python3
""" Module

`1-rectangle`: Contains class `Rectangle`
"""


class Rectangle:
    """ Defines a rectangle w attr `width` and `height`
    """

    def __init__(self, width=0, height=0):
        """Initialise an object
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Returns a property `width`. GETTER
        """
        return self.__width

    @property
    def height(self):
        """Retrieves property `height`. GETTER
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets a property `width`

        Args:
            value (_int_): New property value

        Raises:
            TypeError: If `value` is not an integer or is None
            ValueError: If `value` is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        else:
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

    @height.setter
    def height(self, value):
        """ Sets a property `height`

        Args:
            value (_int_): _New height value_

        Raises:
            TypeError: _If `value` is not an integer or is None_
            ValueError: _If `value` is less than 0_
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
