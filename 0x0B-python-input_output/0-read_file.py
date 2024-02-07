#!/usr/bin/python3
"""fucntion read_file"""


def read_file(filename=""):
    """read from file and print the text"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
