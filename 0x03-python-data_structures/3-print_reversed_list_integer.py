#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    reversed = list()
    if length == 0:
        return
    for item in my_list:
        reversed = [item] + reversed

    for i in range(length):
        print("{:d}".format(reversed[i]))
