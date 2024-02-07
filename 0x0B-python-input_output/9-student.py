#!/usr/bin/python3
"""class Student"""


class Student:
    """method in class"""

    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
