#!/usr/bin/python3
tuple_a = (1, 89)
tuple_b = ()

print("length1 is {:d}".format(len(tuple_a)), end="\n")
print("length2 is {:d}".format(len(tuple_b)), end="\n")

length1 = len(tuple_a)
length2 = len(tuple_b)

if length1 == 1:
    tuple_a = tuple_a + (0,)
elif length1 == 0:
    tuple_a = (0, 0)

if length2 == 1:
    tuple_b = tuple_b + (0,)
elif length2 == 0:
    tuple_b = (0, 0)

print("first: ", tuple_a)
print("second: ", tuple_b)

sum1 = tuple_a[0] + tuple_b[0]
sum2 = tuple_a[1] + tuple_b[1]

c =(sum1, sum2)

print(c)
