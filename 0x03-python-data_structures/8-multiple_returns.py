#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        firstChar = None
    else:
        firstChar = sentence[0]

    return (length, firstChar)
