#!/usr/bin/python3
"""send POST request"""
from requests import post
from sys import argv


if __name__ == "__main__":
    values = {
        'email': argv[2]
    }
    request = post(argv[1], data=values)
    print(request.text)
