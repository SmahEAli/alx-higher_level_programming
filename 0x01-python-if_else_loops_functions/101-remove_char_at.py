#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(str, n):
    #  func that creates a copy of the str, removing the char at the position n

    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
