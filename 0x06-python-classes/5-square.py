#!/usr/bin/python3
"""python3 -c 'print(__import__("4-square").__retrieveSize__)'"""


class Square:
    """python3 -c 'print(__import__("Square").MyClass.__retrieveSize__)'"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be  >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__size):
                    print("{}".format("#"), end='')

                print()
