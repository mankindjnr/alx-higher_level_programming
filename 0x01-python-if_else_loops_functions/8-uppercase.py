#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(0, length):
        if str[i] >= 'a' and str[i] <= 'z':
            print("{:c}".format(ord(str[i]) - 32), end='')
        else:
            print("{:s}".format(str[i]), end='')
    print()
