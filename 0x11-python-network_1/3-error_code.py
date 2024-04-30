#!/usr/bin/python3
"""display error message"""
from urllib import error
from urllib import request
from sys import argv


if __name__ == '__main__':
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
