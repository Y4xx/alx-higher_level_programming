#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from another class"""

    def __init__(self, size):
        """init file access to the parent class method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
