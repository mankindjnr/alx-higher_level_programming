#!/usr/bin/python3
"""python3 -c 'print(__import__("2-matrix_divided").__doc__)')"""


def matrix_divided(matrix, div):
    """python3 -c 'print(__import__("2-matrix_divided").matrix_div.__doc__)'"""
    # checking if the value of the matrix are int or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "integers/floats")

    # check if the rows are equal
    equal_rows = True
    for i in range(len(matrix) - 1):
        if matrix[i] != matrix[i + 1]:
            equal_rows = False
            break
        if equal_rows is False:
            raise TypeError("Each row of the matrix must have the same size")

    # check if div is a float or an int and round to 2d
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    div = round(div, 2)

    # divide the matrix by div
    result = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result
