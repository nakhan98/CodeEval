#!/usr/bin/env python2
# CodeEval - Reverse and Add
# https://www.codeeval.com/open_challenges/45/

from sys import argv

def reverse_add(interger_str):
    reverse_str = interger_str[::-1]
    sum_ = int(interger_str) + int(reverse_str)
    return str(sum_)


def is_palindrome(interger_str):
    if interger_str == interger_str[::-1]:
        return True
    else:
        return False


def main():
    f = open(argv[1], "rt")
    for line in f:
        interger_str = line.strip()
        iterations = 0
        while True:
            interger_str =  reverse_add(interger_str)
            iterations += 1
            if is_palindrome(interger_str):
                print("%d %s" % (iterations, interger_str))
                break

    f.close()


if __name__ == "__main__":
    main()
