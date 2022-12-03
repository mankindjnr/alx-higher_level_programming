#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None

    tempMax = my_list[0]
    for i in range(1, length):
        if tempMax > my_list[i]:
            tempMax = tempMax
        else:
            tempMax = my_list[i]

    return tempMax
