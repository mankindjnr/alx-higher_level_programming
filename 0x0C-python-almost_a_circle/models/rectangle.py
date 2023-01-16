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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
            self.__width = value

        # height
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        # x
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        # y
        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
