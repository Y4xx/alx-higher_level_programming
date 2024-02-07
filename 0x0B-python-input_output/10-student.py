#!/usr/bin/python3
"""class Student"""


class Student:
    """method in class"""

    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            new_dict = {}
            for element in attrs:
                if element in self.__dict__:
                    new_dict[element] = self.__dict__[element]
            return new_dict
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
