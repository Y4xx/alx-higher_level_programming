#!/usr/bin/python3
"""Error code #1"""
from requests import get
from sys import argv


if __name__ == "__main__":
    request = get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
