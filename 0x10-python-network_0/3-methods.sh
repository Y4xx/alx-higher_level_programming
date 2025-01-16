#!/bin/bash
#cURL only methods
curl -s -X OPTIONS -i "$1" | grep "Allow" | cut -d " " -f 2-
