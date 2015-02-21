#!/usr/bin/env python2
# CodeEval Challenge - Reverse Words
# https://www.codeeval.com/open_challenges/8/

import sys

with open(sys.argv[1], 'r') as f:
    lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    words = line.split()[::-1]
    if len(words) == 0: # line is empty
        continue
    
    for word in words:
        sys.stdout.write(word + " ")

    sys.stdout.write("\n")
