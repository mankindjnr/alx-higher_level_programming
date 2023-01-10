#!/usr/bin/python3
"""using with to read a text file and print it to the stdout"""


def read_file(filename=""):
    """the function reading a text file"""
    with open(filename, encoding="utf-8")as read_file:
        print(read_file.read())
