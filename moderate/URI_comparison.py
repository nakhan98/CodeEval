#!/usr/bin/env python2
"""
- CodeEval: URI Comparison
- https://www.codeeval.com/open_challenges/80/
"""

from sys import argv
from urllib import unquote

def decode_url(url):
    """
    - Convert to lowercase
    - Remove port 80
    - Decode hex codes
    """
    url = url.lower()
    url = url.replace(":80", "")
    url = unquote(url)
    return url


def main():
    with open(argv[1]) as fh:
        for line in fh:
            url1, url2 = line.strip().split(';')
            url1 = decode_url(url1)
            url2 = decode_url(url2)
            print(url1 == url2)


if __name__ == "__main__":
    main()
