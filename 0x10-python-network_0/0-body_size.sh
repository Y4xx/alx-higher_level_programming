#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request using curl and retrieve the size of the body in bytes
size=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the body
echo "$size"
