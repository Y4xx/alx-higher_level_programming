#!/usr/bin/python3
"""fucntion check subclass"""


def inherits_from(obj, a_class):
    """sub class"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
