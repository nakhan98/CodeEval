#!/usr/bin/env python2
"""
- CodeEval: Filename Pattern
- https://www.codeeval.com/open_challenges/169/
"""

from fnmatch import fnmatch
from sys import argv


def match_filenames(pattern, file_names):
    match_filenames = []
    for i in file_names:
        if fnmatch(i, pattern):
            match_filenames.append(i)

    return match_filenames
    

def main():
    with open(argv[1]) as f:
        for line in f:
            tokens = line.strip().split(' ')
            pattern = tokens[0]
            file_names = tokens[1:]
            matching_filenames = match_filenames(pattern, file_names)
            if matching_filenames:
                print( ' '.join(matching_filenames) )
            else:
                print('-')


if __name__ == "__main__":
    main()
