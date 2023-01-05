#!/usr/bin/python3
"""a rectangle class that defines a rectangle based on module 2-rectangle.py"""


class Rectangle:
    """clAss defining a rectangle - we count instances created and those del"""
    # public class attribute creation
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    # printing the rectangle shape using str
    def __str__(self):
        print_symbol = '#'
        if self.__width == 0 or self.__height == 0:
            return ''
        return'\n'.join(str(self.print_symbol) * self.__width for _ in
                        range(self.__height))

    # a string representation of the rectangle using __repr__
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # detecting instance deletion
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))

    # static method that creates two instances of rectangle
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
