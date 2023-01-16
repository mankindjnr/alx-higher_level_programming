#!/usr/bin/python3
"""python3 -c 'print(__import__("base").__doc__)'"""


class Base:
    """python3 -c 'print(__import__("base").Base.__doc__)'"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        python3 -c 'print(__import__("base").Base.id manage.__doc__)'
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
