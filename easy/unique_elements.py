#!/usr/bin/env python2
# CodeEval - Unique elements
# https://www.codeeval.com/open_challenges/29/

import sys

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().split("\n")

for line in lines:
    new_list = []
    line = line.strip()
    list_ = line.split(",")

    for i in list_:
        if i in new_list:
            continue
        else:
            new_list.append(i)

    print( ",".join(new_list) )
