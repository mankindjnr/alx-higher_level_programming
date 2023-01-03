#!/usr/bin/python3
"""python3 -c 'print(__import__("5-text_indentation").__doc__)'"""


def text_indentation(text):
    """
    python3 -c 'print(__import__("5-text_indentation").text_indentation.
    __doc__)
    '"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # iterating over each character in the text
    for c in text:
        # print the characters
        print(c, end='')
        # if the character is a. , : break and add two new lines
        if c in ['.', ',', ':']:
            print('\n')
