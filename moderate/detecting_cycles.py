#!/usr/bin/env python2
# CodeEval - Detecting Cycles
# https://www.codeeval.com/open_challenges/5/

import sys

def detect_cycles(line):
    numbers = line.split(" ")
    len_numbers = len(numbers)
    index = 0
    while len(numbers)>1:
        block_size = 1
        while block_size < len_numbers/2:
            numbers_1 = numbers[0:block_size]
            numbers_2 = numbers[block_size:2*block_size]
            if numbers_1 == numbers_2:
                return numbers_1
            else:
                block_size += 1
        
        numbers = numbers[1:]


def main():
    with open(sys.argv[1], "rt") as fh:
        for line in fh:
            line = line.strip()
            reps = detect_cycles(line)
            if reps:
                print( " ".join(reps) )
            else:
                print("")


if __name__ == "__main__":
    main()
