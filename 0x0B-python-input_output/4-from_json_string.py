#!/usr/bin/python3
"""fucntion from_json_string"""
import json


def from_json_string(my_str):
    """returns a Python data structure"""
    return json.loads(my_str)
