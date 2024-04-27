#!/bin/bash
# sends a request to URL and displays the size of the body
curl -s "$1" | wc -c
