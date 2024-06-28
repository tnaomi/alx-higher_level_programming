#!/usr/bin/python3
""" Contains `Base` class """


class Base():
    """ Defines the class `Base` """
    __nb_objects = 0
    def __init__(self, id=None):
        """ Initalise `Base` instance with `id`""" 
        if id is not None and type(id) is int:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects