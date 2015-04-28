#!/usr/bin/env python2
"""
- CodeEval: Overlapping Rectangles
- https://www.codeeval.com/open_challenges/70/
"""

from sys import argv

def get_coordinates(a, b, c, d):
    ''' return coordinate of points in rectangle'''
    p1 = (a,b)
    p2 = (c, b)
    p3 = (c, d)
    p4 = (a, d)
    return (p1, p2, p3, p4)


def rectangles_overlap(rectangle_1, rectangle_2):
    """Check if any points in the triangles fall within the other"""
    # Check if any points in rectangle 1 fall in 2
    points_of_interest = []
    for i in rectangle_1:
        for j in rectangle_2:
            if i[0] >= j[0] and i[1] >= j[1]:
                points_of_interest.append(i)

    if points_of_interest:
        for i in points_of_interest:
            for j in rectangle_2:
                if i[0] <= j[0] and i[1] <= j[1]:
                    return True

    # Check if any points in rectangle 2 fall in 1
    rectangle_1, rectangle_2 = rectangle_2, rectangle_1

    points_of_interest = []
    for i in rectangle_1:
        for j in rectangle_2:
            if i[0] >= j[0] and i[1] >= j[1]:
                points_of_interest.append(i)

    if points_of_interest:
        for i in points_of_interest:
            for j in rectangle_2:
                if i[0] <= j[0] and i[1] <= j[1]:
                    return True


def main():
    with open(argv[1]) as f:
        for line in f:
            points = line.rstrip().split(',')
            points = [int(i) for i in points]
            rect_a = points[:4]
            rect_b = points[4:]
            rect_a_coords = get_coordinates(*rect_a)
            rect_b_coords = get_coordinates(*rect_b)

            if rectangles_overlap(rect_a_coords, rect_b_coords):
                print("True")
            else:
                print("False")


if __name__ == "__main__":
    main()
