#!/usr/bin/python3
"""python3 -c 'print(__import__("4-square").__retrieveSize__)'"""


class Square:
    """python3 -c 'print(__import__("Square").MyClass.__retrieveSize__)'"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be  >= 0")
        self.__size = value

    def position(self, Tup):
        if (len(Tup) != 2 or (not Tup[0].isdigit() or not Tup[1].isdigit())):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = Tup

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for j in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for t in range(self.__position[0]):
                print("{}".format(' '), end='')
            for k in range(self.__size):
                print("{}".format("#"), end='')

            print()
