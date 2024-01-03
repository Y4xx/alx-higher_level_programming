#!/usr/bin/python3
for first in range(0, 9):
    for last in range(first + 1, 10):
        if first != 8:
            print("{}{}".format(first, last), end=", ")
print("89")
