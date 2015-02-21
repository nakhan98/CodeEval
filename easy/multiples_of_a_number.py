#!/usr/bin/env python2
# Codeeval - Multiples of a Number
# https://www.codeeval.com/open_challenges/18/

import sys

def smallest_multiple(x, n):
    orig_n = n
    while n < x:
        n = n + orig_n
    return n


def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    for line in lines:
        numbers = line.split(",")
        numbers = [int(i) for i in numbers]
        x,n = numbers
        print( smallest_multiple(x, n) )


if __name__ == "__main__":
    main()
