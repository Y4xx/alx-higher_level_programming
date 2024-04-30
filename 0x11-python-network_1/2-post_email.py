#!/usr/bin/python3
"""send POST request"""
from urllib import parse
from urllib import request
from sys import argv


if __name__ == '__main__':
    values = {
        'email': argv[2]
    }
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
