#!/usr/bin/python3
def best_score(a_dictionary):
    alist = []

    if a_dictionary is None:
        return None

    for value in a_dictionary.values():
        alist.append(value)

    largest = alist[0]
    for i in range(1, len(alist)):
        if largest < alist[i]:
            largest = alist[i]
            larg = largest

    for key, value in a_dictionary.items():
        if value == larg:
            big = key

    return big
