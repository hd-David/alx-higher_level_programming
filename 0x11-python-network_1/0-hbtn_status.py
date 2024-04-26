#!/usr/bin/python3

import urllib.request


def fetch_status(url):
    """
    Fetches the content of the given URL and displays 
    information about the response body.

    Args:
    - url (str): The URL to fetch.

    Returns:
    - str: The content of the response body.
    """

    # Open the URL using urllib.request.urlopen() and use a 'with'
    # statement to ensure\
    # proper closing of the connection

    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
    print("\t- utf8 content: {}".format(utf8_content))

    
    return body


#URL to fetch
url = urllib.request.Request( 'https://alx-intranet.hbtn.io/status')

# Fetch the status and store the response body in a variable
response_body = fetch_status(url)
