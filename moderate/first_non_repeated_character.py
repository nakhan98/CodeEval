#!/usr/bin/env python2
# CodeEval - First Non-Repeated Character
# https://www.codeeval.com/open_challenges/12/ 

from sys import argv

with open(argv[1], "rt") as f:
    lines = f.readlines()

for line in lines:
    string = line.strip()
    for char in string:
        if string.count(char) == 1:
            print(char)
            break
