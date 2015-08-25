#!/usr/bin/env python2
"""
- CodeEval: Hidden Digits
- https://www.codeeval.com/open_challenges/122/
"""

from sys import argv

ALPHABETS = tuple("abcdefghij")
NUMBERS = tuple([str(i) for i in range(10)])
HIDDEN_DIGITS_MAP = {}


def create_hidden_digits_map():
    global HIDDEN_DIGITS_MAP
    HIDDEN_DIGITS_MAP = dict(zip(ALPHABETS, NUMBERS))


def get_all_digits(string):
    all_digits = []
    for char in string:
        if char in ALPHABETS:
            all_digits.append(HIDDEN_DIGITS_MAP[char])
        elif char in NUMBERS:
            all_digits.append(char)

    return all_digits


def main():
    create_hidden_digits_map()
    with open(argv[1]) as fh:
        for line in fh:
            string = line.rstrip()
            all_digits = get_all_digits(string)
            if all_digits:
                print("".join(all_digits))
            else:
                print("NONE")


if __name__ == "__main__":
    main()
