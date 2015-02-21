#!/usr/bin/env python2
# CodeEval - Fibbonacci Series
# https://www.codeeval.com/open_challenges/22/

import sys

def fibo_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_number(n-1) + fibo_number(n-2)


def main():
    with open(sys.argv[1], 'r') as fh:
        for number in fh:
            number = int(number)
            print( fibo_number(number) )


if __name__ == "__main__":
    main()
