#!/usr/bin/env python
# CodeEval - Longest Common Sequence (incomplete)
# https://www.codeeval.com/public_sc/6/

import sys
import re

def main():
    file_contents = open(sys.argv[1], "rt").readlines()
    file_contents = [i for i in file_contents if not re.search(r"^\s+$", i)] # filter empty lines

    for line in file_contents:
        seq1, seq2 = line.split(";")
        print( find_common_seque
