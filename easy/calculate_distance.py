#!/usr/bin/env python2
# CodeEval - Calculate Distance
# https://www.codeeval.com/open_challenges/99/

import re
from sys import argv

def extract_coords(string):
    '''Extract ccordinates from line'''
    coords = re.findall(r"\((\-?\d+\,\s\-?\d+)\)", string)
    coords_1 = coords[0].split(",")
    coords_1 = [int(i) for i in coords_1]

    coords_2 = coords[1].split(",")
    coords_2 = [int(i) for i in coords_2]

    return (coords_1, coords_2)


def cal_distance(coord_1, coord_2):
    diff_x = coord_1[0] - coord_2[0]
    diff_y = coord_1[1] - coord_2[1]
    distance = (diff_x**2 + diff_y**2)**0.5
    return int(distance)


def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()

    for line in lines:
        coordinates_list = line.strip()
        c1, c2 = extract_coords(line)
        print( cal_distance(c1, c2) )
    

if __name__ == "__main__":
    main()
