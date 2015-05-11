#!/usr/bin/env python2
"""
- CodeEval: Find a Square
- https://www.codeeval.com/open_challenges/101/
"""

from sys import argv
#import pdb
import re


def is_square_old(coords):
    """Determine if given coordinate make a square. 
    Doesn't work with rotated squares"""
    for i in coords:
        x = []
        y = []
        for j in coords:
            if i[0] == j[0]:
                x.append(j)
            if i[1] == j[1]:
                y.append(j)
        if len(x) == 2 and len(y) == 2:
            return True
        else:
            return False


def is_square(coords):
    """ Determine if given coordinates make a square.
    Source for method - http://programmers.stackexchange.com/a/176942"""
    distances = {}
    a, b, c, d = [tuple(i) for i in coords]
    distances[(a,b)] = calc_dist(a,b)
    distances[(a,c)] = calc_dist(a,c)
    distances[(a,d)] = calc_dist(a,d)

    matching_dist_coords = [i for i,j in distances.items() 
            if distances.values().count(j) == 2]

    if len(matching_dist_coords) != 2:
        return False

    other_dist_coords = [i for i in distances if i not in matching_dist_coords]
    other_dist = distances.get(other_dist_coords[0])

    if calc_dist(matching_dist_coords[0][1], matching_dist_coords[1][1]) == other_dist:
        return True
    else:
        return False


def calc_dist(c1, c2):
    diff_x = (c2[0] - c1[0])**2
    diff_y = (c2[1] - c1[1])**2
    dist = (diff_x + diff_y)**0.5
    return dist


def main():
    with open(argv[1]) as f:
        for line in f:
            line = line.strip()
            coords = re.findall(r"\(\-?(\d+,\-?\d+)\)", line)
            coords = [i.split(',') for i in coords]
            coords = [ [int(x) for x in i] for i in coords]
            if is_square(coords):
                print("true")
            else:
                print("false")


if __name__ == "__main__":
    main()
