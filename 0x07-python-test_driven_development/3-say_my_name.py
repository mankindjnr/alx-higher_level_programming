#!/usr/bin/python3
"""python3 -c 'print(__import__("3-say_my_name").__doc__)'"""


def say_my_name(first_name, last_name=""):
    """python3 -c 'print(__import__("3-say_my_name").say_my_name.__doc__)'"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
