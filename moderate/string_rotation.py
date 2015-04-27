#!/usr/bin/env python2
"""
- CodeEval: String Rotation
- https://www.codeeval.com/open_challenges/76/
- This one was annoying as there wasn't any explanation of what "string rotation" was
"""

from sys import argv

def is_rotation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    concat_string = string_1 + string_1
    if string_2 in concat_string:
        return True
    else:
        return False


def main():
    with open(argv[1]) as f:
        for line in f:
            string_1, string_2 = line.rstrip('\n').split(',')
            if is_rotation(string_1, string_2):
                print("True")
            else:
                print("False")


if __name__ == "__main__":
    main()
