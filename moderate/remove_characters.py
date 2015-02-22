#!/usr/bin/env python2
# CodeEval - Remove Characters
# https://www.codeeval.com/open_challenges/13/

from sys import argv

def scrub_string(string, scrub_chars):
    '''Scrub string of of scrub_chars'''
    scrub_chars = scrub_chars.strip()
    for char in scrub_chars:
        string = string.replace(char, "")

    return string


def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()

    for line in lines:
        string, scrub_chars = line.strip().split(",")
        print(scrub_string(string, scrub_chars))


if __name__ == "__main__":
    main()
