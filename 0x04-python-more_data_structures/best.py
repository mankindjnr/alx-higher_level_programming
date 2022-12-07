#!/usr/bin/python3
def best_score(a_dictionary):
    aList = []

    if len(a_dictionary) == 0:
        return None

    for value in a_dictionary.values():
        aList.append(value)

    maxI = aList[0]
    for i in range(1, len(aList)):
        if maxI < aList[i]:
            maxI = aList[i]

    for key, value in a_dictionary.items():
        if value == maxI:
            big = key

    return big
