#!/usr/bin/python3
"""a function that writes to a text file and returns the characters num"""


def write_file(filename="", text=""):
    """the function that writes to a file or creats one if non-existent"""
    with open(filename, mode="w", encoding="utf-8")as write_file:
        write_file.write(text)

        num_of_chars = len(text)
        return num_of_chars
