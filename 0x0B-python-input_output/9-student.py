#!/usr/bin/python3
""" Contains class `Student` w `__init__` & `to_json` """


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

    def to_json(self):
        """ Returns a dictionary represantation of `Student` instance """
        return self.__dict__
