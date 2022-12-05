#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            if j == 2:
                print(matrix[i][j], sep="\n")
            else:
                print(matrix[i][j], end=' ')
