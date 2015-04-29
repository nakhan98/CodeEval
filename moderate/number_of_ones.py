#!/usr/bin/env python2

"""
- CodeEVal: Number of Ones
- https://www.codeeval.com/open_challenges/16/
"""

from sys import argv

def ones_in_bin(number):
    binary = bin(number)
    binary = str(binary)[2:]
    return binary.count('1')
    

def main():
    with open(argv[1]) as f:
        for line in f:
            number = int(line)
            print( ones_in_bin(number) )

if __name__ == "__main__":
    main()
