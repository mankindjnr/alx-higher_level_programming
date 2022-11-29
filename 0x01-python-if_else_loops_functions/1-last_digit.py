#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

numberCopy = number

if numberCopy < 0:
    numberCopy = numberCopy * -1
    last = (numberCopy % 10) * -1
else:
    last = number % 10

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif ((last != 0) and (last < 6)):
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
