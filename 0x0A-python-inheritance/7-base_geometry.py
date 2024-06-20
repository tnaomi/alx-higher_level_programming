#!/usr/bin/python3
""" Contains a class `BaseGeometry` w public instance methods """


class BaseGeometry():
    """ Defines `BaseGeometry` w public instance attr `area`
    and `integer_validator`
    """
    def area(self):
        """ Unimplemented method. Raises an `Exception` """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates `value`. `name` assumed as string """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
