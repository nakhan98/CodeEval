#!/usr/bin/env python2
"""
- CodeEval: Read More
- https://www.codeeval.com/open_challenges/167/
"""

from sys import argv

MAX_LEN = 55
TRIM_LEN = 40
APPEND_STRING = "... <Read More>"

def shorten_line(line):
    """
    Modify line that is over 55 chars according to challenge specs
    """
    new_line = ""
    tokens = line.split(' ')
    for word in tokens:
        temp = new_line + "%s " % word
        temp.rstrip()
        if len(temp) > TRIM_LEN:
            new_line = new_line.rstrip() + APPEND_STRING
            break
        else:
            new_line = temp

    if new_line == APPEND_STRING:
        return line[:TRIM_LEN] + APPEND_STRING
    else:
        return new_line
        

def main():
    with open(argv[1]) as fh:
        for line in fh:
            line = line.rstrip()
            if len(line) > MAX_LEN:
                print(shorten_line(line))
            else:
                print(line)


if __name__ == "__main__":
    main()
