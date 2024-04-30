#!/usr/bin/python3
""" use method .info() to get the headers(response object)"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
        