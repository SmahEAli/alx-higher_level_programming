#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list
    Return real number of elements printed
    """

    n_e= 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            n_e += 1
        except IndexError:
            break
    print("")
    return (n_e)
