#!/usr/bin/python3
""" Module

`8-rectangle`: Contains class `Rectangle`
"""


class Rectangle:
    """ Defines a rectangle w private attr `width` and `height`
    and public attr `number_of_instances` and `print_symbol`
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise an object

        Args:
            width (_int_): Defaults to 0
            height (_int_): Defaults to 0
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self) -> str:
        """ Returns string of `self` object

        Returns:
            str: str representation of a rectangle with the
            character in `print_symbol`
        """
        str_list = []
        if self.width == 0 or self.height == 0:
            str_list = []
        else:
            for i in range(self.height):
                for k in range(self.width):
                    str_list.append("{}".format(self.print_symbol))
                if i != self.height - 1:
                    str_list.append("{:s}".format("\n"))
        return "".join(str_list)

    def __repr__(self) -> str:
        """ Returns a string representation of `Rectangle` for use w `eval()`

        Returns:
            str: _String representation_
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.width))

    def __del__(self):
        """ Print a msg when an instance of `Rectangle` is being deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return Rectangle.number_of_instances

    def bigger_or_equal(rect_1, rect_2):  # type: ignore
        """ Compare rectangles based on `area`

        Args:
            rect_1 (_object_): First `Rectangle` instance
            rect_2 (_object_): Second `Rectangle` instance

        Raises:
            TypeError: If `rect_1` or `rect_2`is not a `Rectangle` instance

        Returns:
            _obj_: _The bigger `Rectangle` instance_
        """
        error = "rect_1 must be an instance of Rectangle"
        if not isinstance(rect_1, Rectangle):
            raise TypeError(error)
        elif not isinstance(rect_2, Rectangle):
            raise TypeError(error.replace("rect_1", "rect_2"))
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
