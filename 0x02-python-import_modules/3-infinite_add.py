#!/usr/bin/python3

if __name__ == "__main__":
    """func that Prints the addition of all argumentS"""
    import sys
    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
