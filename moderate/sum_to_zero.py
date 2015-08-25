#!/usr/bin/env python2
"""
- CodeEval: Sum to Zero
- https://www.codeeval.com/open_challenges/81/
"""

from sys import argv
from itertools import combinations

N = 4

def find_sums_to_zero(numbers, n):
    """
    Find and return combinations of n
    which sum to zero
    """
    combs_to_zero = []
    for comb in combinations(numbers, n):
        if sum(comb) == 0:
            combs_to_zero.append(comb)
    return combs_to_zero


def main():
    with open(argv[1]) as fh:
        for line in fh:
            numbers = line.rstrip().split(',')
            numbers = [int(i) for i in numbers]
            sums_to_zero = find_sums_to_zero(numbers, N)
            print(len(sums_to_zero))


if __name__ == "__main__":
    main()
