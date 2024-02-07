#!/usr/bin/python3
"""class Mylist"""


class MyList(list):
    """print sorted list"""

    def print_sorted(self):
        print(sorted(list(self)))
