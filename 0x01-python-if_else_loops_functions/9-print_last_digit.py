#!/usr/bin/python3
def print_last_digit(number):
    numberCopy = number

    if number < 0:
        numberCopy = numberCopy * -1
        return numberCopy % 10
    else:
        return number % 10
