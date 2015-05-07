#!/usr/bin/env python2
"""
- CodeEval - Split the Number
- https://www.codeeval.com/open_challenges/131/
"""

from sys import argv

def do_calc(n, pattern):
    if '+' in pattern:
        sign = '+'
        index_sign = pattern.index('+')
    else:
        sign = '-'
        index_sign = pattern.index('-')

    x, y = int( n[:index_sign] ), int( n[index_sign:] )
    if sign == '+':
        return x+y
    else:
        return x-y
    

def main():
    with open(argv[1]) as f:
        for line in f:
            n, pattern = line.strip().split(' ')
            result = do_calc(n, pattern)
            print(result)

if __name__ == "__main__":
    main()
