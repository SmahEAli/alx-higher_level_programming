#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list

     Args:
        my_list (list): list
        x (int): no. of elements to print

        Returns:
        no.of elements printed
        """

    x_e = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            x_e += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (x_e)
