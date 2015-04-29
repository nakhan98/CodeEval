#!/usr/bin/env python2
"""
- CodeEval: Point in Circle
- https://www.codeeval.com/open_challenges/98/
"""

from sys import argv
import re
import math

def extract_data(line):
    """Extract center, radius and point data from a line"""
    #pdb.set_trace()
    center, radius, point = line.rstrip().split(';')
    center = re.findall(r"([\-\d\.]+)", center)
    center = [float(i) for i in center]
    radius = re.search(r"([\-\d\.]+)", radius).group(1)
    radius = float(radius)
    point = re.findall(r"([\-\d\.]+)", point)
    point = [float(i) for i in point]
    return (center, radius, point)


def point_in_circle(center, radius, point):
    _ = pow((point[0] - center[0]), 2) + pow((point[1] - center[1]), 2)
    distance = math.sqrt(_)
    if distance < radius:
        return True
    else:
        return False


def main():
    with open(argv[1]) as f:
        for line in f:
            center, radius, point = extract_data(line)
            if point_in_circle(center, radius, point):
                print("true")
            else:
                print("false")


if __name__ == "__main__":
    main()
