#!/usr/bin/python3
"""fucntion load_from_json_file"""
import json


def load_from_json_file(filename):
    """return Object from JSON"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
