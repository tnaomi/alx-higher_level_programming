#!/usr/bin/python3
""" Module

`2-rectangle`: Contains class `Rectangle`
"""


class Rectangle:
    """ Defines a rectangle w attr `width` and `height`
    """

    def __init__(self, width=0, height=0):
        """Initialise an object
        """
        self.__width = width
        self.__height = height

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
        elif value < 0:
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
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Calculates an `area` of a rectangle

        Returns:
            _int_: _An `area` of a rectange_
        """
        return self.width * self.height

    def perimeter(self):
        """ Calculates the perimeter of a rectangle

        Returns:
            _int_: _`Perimeter`_
        """
        return 2 * self.width + 2 * self.height
