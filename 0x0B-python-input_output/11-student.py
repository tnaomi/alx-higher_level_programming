#!/usr/bin/python3
""" Contains class `Student` w `__init__` & `to_json(self, attrs)` """


class Student():
    """ Defines class `Student` """
    def __init__(self, first_name, last_name, age):
        """ Initialises `Student` w `first_name`, `last_name`, `age` """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary represantation of `Student` instance """
        if not isinstance(attrs, (list)) or not all(isinstance(i, str)
                                                    for i in attrs):
            return self.__dict__.copy()
        else:
            new_d = {i: self.__dict__[i] for i in attrs if i in self.__dict__}
            return new_d

    def reload_from_json(self, json):
        """ Replaces an instance w JSON data """
        self.__setattr__("last_name", json.get("last_name"))
        self.__setattr__("first_name", json.get("first_name"))
        self.__setattr__("age", json.get("age"))
