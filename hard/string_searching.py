#!/usr/bin/env python
# CodeEval - String Searching (incomplete)
# https://www.codeeval.com/open_challenges/28/

import sys
import re
#import ipdb

def is_substr(x, y):
    ''' Determine if y is a substring of x.
        Assuming both '*' and '\*' not in same line'''
    
    #ipdb.set_trace()
    if "*" in y and "\*" not in y:
        y = y.replace("*", "\w*")
        #print(y)
        if re.search(y, x):
            return "true"
    elif "\*" in y:
        y = y.replace("\*", "*")
        if re.search(y, x):
            return "true"
    else:
        if re.search(y, x):
            return "true"
    
    return "false"
    

def main():
    with open(sys.argv[1], "rt") f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        seq1, seq2 = line.split(",")
        print( is_substr(seq1, seq2) )


if __name__ == "__main__":
    main()
