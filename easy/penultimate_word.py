#!/usr/bin/env python2
# CodeEval - Penultimate Word
# https://www.codeeval.com/open_challenges/92/

from sys import argv

with open(argv[1], "rt") as f:
    lines = f.readlines()

for line in lines:
    words = line.strip().split()
    print(words[-2])
