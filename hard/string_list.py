#!/usr/bin/env python
# CodeEval - String List
# https://www.codeeval.com/open_challenges/38/

from sys import argv
from itertools import product

def gen_combs(length, chars):
    combs = set(product(chars, repeat=length))
    combs = ["".join(i) for i in combs]
    return combs


def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()

    for line in lines:
        string_list = []
        n, string = line.strip().split(",")
        combinations = gen_combs(int(n), list(string))
        combinations = sorted(combinations)
        print(",".join(combinations))


if __name__ == "__main__":
    main()
