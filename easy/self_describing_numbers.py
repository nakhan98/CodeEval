#!/usr/bin/env python2
# Self describing numbers
# https://www.codeeval.com/open_challenges/40/

import sys

def is_self_describing(number_string):
    number_length = len(number_string)
    number = int(number_string)
    i = 0
    while i < number_length:
        x = number_string[i]
        if number_string.count( str(i) ) != int(x):
            return 0

        i += 1

    return 1


def main():
    with open(sys.argv[1], 'r') as f:
        for number in f:
            print( is_self_describing(number.strip()) )


if __name__ == "__main__":
    main()            
