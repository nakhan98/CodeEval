#!/usr/bin/env python
# CodeEval - Array Absurdity
# https://www.codeeval.com/open_challenges/41/

from sys import argv

with open(argv[1], "rt") as f:
    lines = f.readlines()

for line in lines:
    N, numbers_string = line.strip().split(";")
    numbers = numbers_string.split(",")
    for i in numbers:
        if numbers.count(i) > 1:
            print(i)
            break

