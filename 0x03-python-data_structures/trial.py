#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

length = len(matrix)

for i in range(length):
    for j in range(length):
        if j == 2:
            print(matrix[i][j], sep="\n")
        else:
            print(matrix[i][j], end=' ')
