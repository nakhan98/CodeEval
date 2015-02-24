#!/usr/bin/env python2
# CodEval - Number Pairs
# https://www.codeeval.com/open_challenges/34/

from itertools import combinations
from sys import argv

def convert_tuple_to_string(pair):
    '''convert number pair tuple to comma separated string'''
    _ = [str(i) for i in pair]
    number_string = ",".join(_)
    return number_string


def find_number_pairs(int_list, X):
    '''Return number pairs from int_list which add up to X'''
    pairs = []
    combs = combinations(int_list, 2)
    for comb in combs:
        if X == (comb[0] + comb[1]):
            pairs.append(comb)
    return pairs


def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()
    
    for line in lines:
        numbers, X = line.strip().split(";")
        numbers = [int(i) for i in numbers.split(",")]
        number_pairs = find_number_pairs(numbers, int(X))
        if not len(number_pairs):
            print("NULL")
        else:
            _ = [convert_tuple_to_string(i) for i in number_pairs]
            print(";".join(_))


if __name__ == "__main__":
    main()
