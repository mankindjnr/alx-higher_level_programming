#!/usr/bin/python3
"""appending a string at the end of a file and return the num of char added"""


def append_write(filename="", text=""):
    """functions appends text at the end of a file"""
    with open(filename, mode="a", encoding="utf-8")as appended:
        appended.write(text)

        num_of_appended_text = len(text)
        return(num_of_appended_text)
