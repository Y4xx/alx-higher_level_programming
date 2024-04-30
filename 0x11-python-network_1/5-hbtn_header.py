#!/usr/bin/python3
"""sends a request to the URL"""
from requests import get
from sys import argv


if __name__ == "__main__":
    request = get(argv[1])
    print(request.headers.get("X-Request-Id"))
