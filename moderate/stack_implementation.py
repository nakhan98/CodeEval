#!/usr/bin/env python2
# CodeEval - Stack Implementation
# https://www.codeeval.com/open_challenges/9/

import sys

def push(list_x, int_y):
    '''Append int to list'''
    list_x.append(int_y)


def pop(list_x):
    '''Remove and return last item in list'''
    last_int = list_x[-1]
    del(list_x[-1])
    return last_int


def print_alternate_ints(list_x):
    while True:
        try:
            sys.stdout.write( str(pop(list_x)) + " " )
            pop(list_x)
        except:
            print("")
            return


def main():
    with open(sys.argv[1], "rt") as f:
        lines = f.readlines()

    for line in lines:
        ints = line.strip().split()
        int_list = []

        for int_ in ints:
            push(int_list, int_)

        print_alternate_ints(int_list)


if __name__ == "__main__":
    main()
