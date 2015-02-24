#!/usr/bin/env python
# CodeEval - String Searching (partial)
# https://www.codeeval.com/open_challenges/28/

import sys
from fnmatch import fnmatch

def is_substr(x, y):
    y = "*" + y + "*"
    if fnmatch(x, y):
        return "true"
    else:
        return "false"
    

def main():
    with open(sys.argv[1], "rt") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        seq1, seq2 = line.split(",")
        print( is_substr(seq1, seq2) )


if __name__ == "__main__":
    main()
