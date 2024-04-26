#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys


"""Sends a POST request to a given URL with a given email."""

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'Your email is' : email}).encode('ascii')
reque = urllib.request.Request(url, data)

with urllib.request.urlopen(reque) as response:
    body = response.read().decode('uft-8')
    print(body)
