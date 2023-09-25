#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(x, y, z):
    # the same as the following Python bytecode

    if x < y:
        return (z)
    if z > y:
        return (x + y)
    return (x*y - z)
