#!/usr/bin/env python2
# CodeEval - String Permutations
# https://www.codeeval.com/open_challenges/14/

import sys
from itertools import permutations

def generate_permutations(string):
    ''' Generate and return a list of sorted permutations'''
    perms = ["".join(i) for i in permutations(string)]
    sorted_perms = sorted(perms)
    return sorted_perms


def main():
    lines = open(sys.argv[1], "rt").readlines()
    for line in lines:
        string = line.strip()
        permutations = generate_permutations(string);
        permutations_string = ",".join(permutations)
        print(permutations_string)


if __name__ == "__main__":
    main()
