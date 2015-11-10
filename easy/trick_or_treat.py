#!/usr/bin/env python2
"""
- CodeEval: Trick or Treat
- https://www.codeeval.com/open_challenges/220/
"""

from sys import argv


COSTUME_CANDIES = {
    "Vampires": 3,
    "Zombies": 4,
    "Witches": 5
}


def get_testcase(line):
    """
    Convert testcase line into a dict and return it
    """
    _ = [i.split(':') for i in line.split(',')]
    _ = [(i.strip(), int(j)) for i,j in _]
    return dict(_)


def calc_total_sweets(testcase):
    """
    Calculate and return total number of sweets from testcase dict
    """
    total_sweeties = 0
    for key, value in COSTUME_CANDIES.iteritems():
        sweeties = testcase[key] * value
        total_sweeties += sweeties

    total_sweeties = total_sweeties * testcase["Houses"]
    return total_sweeties


def calc_candies_per_kid(total_sweets, testcase):
    """
    Calculate the number of candies per child
    """
    kids = sum(testcase[k] for k in COSTUME_CANDIES)
    return total_sweets/kids


def main():
    with open(argv[1]) as fh:
        for line in fh:
            testcase = get_testcase(line.rstrip())
            total_sweets = calc_total_sweets(testcase)
            candies_per_kid = calc_candies_per_kid(total_sweets, testcase)
            print(candies_per_kid)
            

if __name__ == "__main__":
    main()
