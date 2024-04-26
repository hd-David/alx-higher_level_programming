#!/usr/bin/python3

import urllib.request
import sys


"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(request_id)
        else:
            print('X-Request-Id not found in the response headers.')
except urllib.error.URLError as e:
    print("Error fetching URL:", e.reason)
    sys.exit(1)
