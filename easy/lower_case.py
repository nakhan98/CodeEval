#!/usr/bin/env python2
# CodeEval - Lowercase
# https://www.codeeval.com/open_challenges/20/

import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        print(line.lower())
