#!/usr/bin/env python
# CodeEval - Sum of digits
# https://www.codeeval.com/open_challenges/21/

import sys

def calculate_sum(number_string):
    sum = 0
    for i in number_string:
        sum += int(i)
    return sum
    

def main():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print(calculate_sum(line.strip()))


if __name__ == "__main__":
    main()
