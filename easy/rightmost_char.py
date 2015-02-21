#!/usr/bin/env python2
# Rightmost Char
# https://www.codeeval.com/open_challenges/31/

import sys

with open(sys.argv[1], "r") as f:
    file_contents = f.readlines()

for line in file_contents:
    string_s, t = line.strip().split(",")
    if t in string_s:
        print( string_s.index(t) )
    else:
        print(-1)
