#!/usr/bin/python3
"""python3 -c 'print(__import__("0-add_integer").__doc__)')"""
def add_integer(a, b=98):
    """python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    add = a + b
    return add
