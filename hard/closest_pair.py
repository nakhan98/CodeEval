#!/usr/bin/env python2
# CodeEval - Closest Pair
# https://www.codeeval.com/open_challenges/51/

from sys import argv
from itertools import combinations

def calc_distance(c1, c2):
    x_diff = c1[0] - c2[0]
    y_diff = c1[1] - c2[1]
    distance = (x_diff**2 + y_diff**2)**0.5
    return distance


def convert_to_coords(string):
    '''Takes string 'x y' and return tuple of integers - (x,y)'''
    coords = string.split(' ') 
    coords = [int(i) for i in coords]
    return tuple(coords)


def obtain_distances(coords_list):
    '''Generate two item combinations of coords and then calculate lowest 
       distance from them'''
    dist = 10000
    combinations_ = combinations(coords_list, 2)
    #combinations_ = list(combinations_) ## oom error
    for i in combinations_:
        _ = calc_distance(*i)
        if _ < dist:
            dist = _
    if dist >= 10000:
        return "infinity"
    else:
        dist_string = "%.4f" % dist
        return dist_string
    

def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        number_of_points = int( lines[i].strip() )
        i += 1
        coords_string = lines[i:i+number_of_points]
        coords = [convert_to_coords(_) for _ in coords_string]
        if len(coords) == 0:
            continue

        lowest_distance = obtain_distances(coords)
        print(lowest_distance)
        i = number_of_points + i 


if __name__ == "__main__":
    main()
