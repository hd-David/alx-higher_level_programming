#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request

def fetch_url(url):
    """Fetches the URL and handles HTTP errors."""
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            return response.read().decode("ascii")
    except urllib.error.HTTPError as e:
        return "Error code: {}".format(e.code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    print(fetch_url(url))
    
