#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """function that raise an error message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
