#!/usr/bin/python3
""" Contains class `Student` w `__init__` & `to_json(self, attrs)` """


class Student():
    """ Defines class `Student` """
    def __init__(self, first_name, last_name, age):
        """ Initialises `Student` w `first_name`, `last_name`, `age` """
        if type(first_name) is not str:
            raise TypeError("first name must be a string")
        elif type(last_name) is not str:
            raise TypeError("last name must be a string")
        elif type(age) is not int:
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("age must be a positive number")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary represantation of `Student` instance """
        if attrs is None:
            return self.__dict__
        else:
            attributes, values, new_dict = attrs.copy(), [], {}
            for i in attributes:
                if i not in self.__dict__:
                    attributes.remove(i)
            values.extend(self.__dict__.get(i) for i in attributes)
            for i in range(len(attributes)):
                new_dict.__setitem__(attributes[i], values[i])
            self.__dict__ = new_dict.copy()
            return self.__dict__
