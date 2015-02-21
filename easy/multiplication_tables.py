#!/usr/bin/env python2
# CodeEval - Multiplication tables
# https://www.codeeval.com/open_challenges/23/

import sys

for i in range(1,13):
    string = ""
    for multiplier in range(1,13):     
        string += str(i*multiplier).rjust(4)  
    string = string.rstrip()
    sys.stdout.write(string +"\n")
