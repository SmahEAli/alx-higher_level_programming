#!/usr/bin/python3
#9-print_last_digit.py
def print_last_digit(n):
    # prints and return last digit of a number

    print(abs(n) % 10, end="")
    return (abs(n) % 10)
