#!/usr/bin/env python2
# CodeEval - Mth to last element 
# https://www.codeeval.com/open_challenges/10/

from sys import argv
import re

def split_chars_index(string):
    ''' Split the chars and integer from string and return them in tuple'''
    results = re.search(r"([\w\s]+)\s(\d+)", string)
    return (results.group(1), results.group(2))


def main():
    with open(argv[1], "rt") as fh:
        for line in fh:
            string = line.rstrip()
            chars, reverse_index = split_chars_index(string)
            reverse_index = int(reverse_index)
            chars = chars.split()
        
            if reverse_index > len(chars):
                continue
            else:
                reverse_index = reverse_index * -1
                print(chars[reverse_index])


if __name__ == "__main__":
    main()
