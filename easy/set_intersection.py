#!/usr/bin/env python2
# CodeEval - Set Intersects
# https://www.codeeval.com/open_challenges/30/

import sys

def show_intersects(list_1, list_2):
    intersect_list = [i for i in list_1 if i in list_2]
    if len(intersect_list) == 0:
        return None
    intersect_list = [ int(i) for i in intersect_list ]
    intersect_list.sort()
    return intersect_list


def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        string_1, string_2 = line.split(";")
        list_1 = string_1.split(",")
        list_2 = string_2.split(",")
        intersects = show_intersects(list_1, list_2)

        if not intersects:
            print("")
        else:
            print(",".join( [str(i) for i in intersects] ))


if __name__ == "__main__":
    main()
