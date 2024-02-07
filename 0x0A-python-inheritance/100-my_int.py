#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """invert equality and inequality"""
    def __eq__(self, other):
        """Invert the == operator's logic"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Invert the != operator's logic"""
        return int.__eq__(self, other)
