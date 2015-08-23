#!/usr/bin/env python2
"""
- CodeEval: URI Comparison
- https://www.codeeval.com/open_challenges/80/
"""

from sys import argv
from urllib import quote, unquote

SAFE_CHARS = ",/?:@&=+$#"

def process_url(url):
    """
    - Convert to lowercase
    - Remove port 80
    - do hex encoding
    """
    url = url.lower()
    url = url.replace(":80", "")
    url = quote(url, safe=SAFE_CHARS)
    return url


def main():
    with open(argv[1]) as fh:
        for line in fh:
            url1, url2 = line.strip().split(';')
            url1 = process_url(unquote(url1))
            url2 = process_url(unquote(url2))
            print(url1 == url2)


if __name__ == "__main__":
    main()
