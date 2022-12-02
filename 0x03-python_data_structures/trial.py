#!/usr/bin/python3
a = [1, 2, 3, 4]
b = []
for i in range(0, len(a)):
    b.append(a[i])

b[0] = 9
print(a)
print(b)

