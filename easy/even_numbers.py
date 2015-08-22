#!/usr/bin/env python2
"""
- CodeEval: Even Numbers
- https://www.codeeval.com/open_challenges/100/
"""

from sys import argv

def main():
    with open(argv[1]) as fh:
        for line in fh:
            number = int(line)
            modulo = number % 2
            if modulo:
                print(0)
            else:
                print(1)


if __name__ == "__main__":
    main()
