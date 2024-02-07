#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """empty class"""

    def __init__(self) -> None:
        """init fucntion none"""
        pass

    def area(self):
        """function that raise an error message """
        raise Exception("area() is not implemented")
