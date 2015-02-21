#!/usr/bin/env python2
# CodeEval - SUM OF INTEGERS FROM FILE
# https://www.codeeval.com/open_challenges/24/

import sys

sum = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        integer = int(line)
        sum += integer

print(sum)
