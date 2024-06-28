#!/usr/bin/python3
""" Contains the class Rectangle #0"""
from models.base import Base


class Rectangle(Base):
    """ Defines the class Rectangle for #0 """
    @classmethod
    def validate(cls, name, value):
        """ Validate `init` """
        msg_t = f"{name} must be an integer"
        msg_v = f"{name} must be {{}} 0"
        if type(value) is not int:
            raise TypeError(msg_t)
        if name == "x" and value < 0:
            raise ValueError(msg_v.format(">="))
        if name == "y" and value < 0:
            raise ValueError(msg_v.format(">="))
        if name not in ["x", "y"] and value <= 0:
            raise ValueError(msg_v.format(">"))
        return value
            
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialises `Rectangle` w
        
        Args:
            width(int)  : width of the `Rectangle`
            height(int) : height of the `Rectangle`
            x(int)      : x-axis. Initialises to 0
            y(int)      : y-axis. Initialises to 0
            id(int)     : Unique `id`. Defaults to `None`
        """
        super().__init__(id)
        self.__width  = self.validate('width', width)
        self.__height = self.validate('height', height)
        self.__x, self.__y =  self.validate('x', x), self.validate('y', y)

    @property
    def width(self):
        """ width GETTER """
        return self.__width

    @width.setter
    def width(self, value):
        """ width SETTER """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """ height GETTER"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height SETTER """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x GETTER"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x SETTER"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """ y GETTER"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of a `Rectangle` """
        return self.width * self.height

    def display(self):
        """ Display `#` as the representation of an instance `Rectangle` #0 """
        for i in range(self.height):
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns a string representation of `Rectangle` """
        return f"[Rectangle] ({self.id!r}) {self.x!r}/{self.y!r} - {self.width!r}/{self.height!r}"

    def update(self, *args):
        """ Updates `Rectangle` instance variables #0 """
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            i = 0
            while i < len(args):
                if i == 0:
                    super().__init__(args[0])                
                else:
                    self.__setattr__(attrs[i], args[i])
                i += 1
        pass
        