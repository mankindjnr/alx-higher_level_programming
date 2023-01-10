#!/usr/bin/python3
"""writing a class student that defines a student"""


class Student:
    """the class student to define a stdent"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, str):
            attrs = [attrs]
            # elif isinstance(attrs, list) and all(isinstance(i, str) for i in att
        else:
            dictionary = {}
            for key in self.__dict__:
                dictionary[key] = self.__dict__[key]

            return dictionary
        # else:
          #  return self.__dict__
