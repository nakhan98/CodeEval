#!/usr/bin/env python2
# CodeEval - Longest Lines
# https://www.codeeval.com/open_challenges/2/

import sys

def find_longest_lines(n,lines):
    ''' Return the longest n lines'''
    lines = [i.strip() for i in lines] # strip newlines
    sorted_lines = sorted(lines, reverse=True, key=len)
    return sorted_lines[:n]


def main():
    with open(sys.argv[1], "rt") as f:
        file_contents = f.readlines()

    no_of_lines = int( file_contents[0].strip() )
    file_contents = file_contents[1:]
    longest_lines = find_longest_lines(no_of_lines, file_contents)

    for line in longest_lines:
        print(line)


if __name__ == "__main__":
    main()
