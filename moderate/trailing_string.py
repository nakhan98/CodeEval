#!/usr/bin/env python2
# CodeEval - Trailing String
# https://www.codeeval.com/open_challenges/32/

from sys import argv

with open(argv[1], "rt") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if line == "":
        continue
    str1, str2 = line.split(",")
    if str1.endswith(str2):
        print(1)
    else:
        print(0)
