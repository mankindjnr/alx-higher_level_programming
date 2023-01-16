#!/usr/bin/python3
"""python3 -c 'print(__import__("rectangle").__doc__)'"""
from models.base import Base


class Rectangle(Base):
    """python3 -c 'print(__import__("rectangle").Rectangle.__doc__)'"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        python3 -c 'print(__import__("rectangle").Rectangle.init.__doc__)'
        """
        # calling super class with id
        super().__init__(id)
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if type(height) is int:
            self.__height = height
        else:
            raise TypeError("height must be an integer")

        if type(x) is int:
            self.__x = x
        else:
            raise TypeError("x must be an integer")

        if type(y) is int:
            self.__y = y
        else:
            raise TyperError("y must be an integer")

        """
        we are using private attributes instead of public  attributes because
        we want to protect attributes of our class. with a setter, you are able
        to validate what developer is trying to assign to a variable so you can
        trust these attributes
        """
        # width
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("{} must be an integer".format("width"))
            if value <= 0:
                raise ValueError("{} must be > 0".format("width"))
            self.__width = value

        # height
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("{} must be an integer".format("height"))
            if value <= 0:
                raise ValueError("{} must be > 0".format("height"))
            self.__height = value

        # x
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError("{} must be an integer".format("x"))
            if value < 0:
                raise ValueError("{} must be >= 0".format("x"))
            self.__x = value

        # y
        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) is not int:
                raise TypeError("{} must be an integer".format("y"))
            if value < 0:
                raise ValueError("{} must be > 0".format("y"))
            self.__y = value

        # area of the rectangle
    def area(self):
        return (self.__height * self.__width)

    # printing the rectangle
    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    # overidding the str method to print a string
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, \
                                                       self.__y, self.__width, \
                                                       self.__height)
