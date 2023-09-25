#!/usr/bin/python3
#6-print_comb3.py
# prints all possible different combinations of two digits, while they must be different

for d in range(0, 10):
    for d_1 in range(d + 1, 10):
        if d == 8 and d_1 == 9:
            print("{}{}".format(d, d_1))
        else:
            print("{}{}".format(d, d_1), end=", ")
