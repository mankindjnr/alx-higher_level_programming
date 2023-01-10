#!/usr/bin/python3
"""using with to read a text file and print it to the stdout"""


def read_file(filename=""):
    """
    the function reading a text file
    with open(filename, mode="r", encoding="utf-8")as read_file:
        print(read_file.read())
    """
    with open(filename)as read_file:
        for line in read_file:
            print(line, end='')
