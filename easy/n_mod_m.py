#!/usr/bin/env python2
# CodeEval - N MOD M
# https://www.codeeval.com/open_challenges/62/

import sys

def mod(x,y):
    orig_x = x
    multiplier = 1

    while x < y:
        multiplier +=1
        x = orig_x*multiplier
    
    if x == y:
        return 0
    else:
        x = x - orig_x
        return y-x


def main():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            y, x = [ int(i) for i in line.strip().split(",") ]
            print( mod(x,y) )


if __name__ == "__main__":
    main()
