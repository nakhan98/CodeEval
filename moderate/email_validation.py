#!/usr/bin/env python2
# CodeEval - Email validation
# https://www.codeeval.com/public_sc/35/

import sys
import re

def is_email(string):
    if re.search(r"^[\w\_\-\.\+]+@[\w\_\-\.]+\.\w+(\.\w+)?$", string):
        return "true"
    else:
        return "false"


def main():
    lines = open(sys.argv[1], "rt").readlines()
    lines = [i.strip() for i in lines if not re.search(r"^\s+$", i) ]
    for line in lines:
        print(is_email(line))


if __name__ == "__main__":
    main()
