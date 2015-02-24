#!/usr/bin/env python2
# CodeEval - Sum of Integers (Partially correct)
# https://www.codeeval.com/open_challenges/17/

from sys import argv

def largest_sum(int_list):
    if len(int_list) == 1:
        return int_list[0]

    sum_ = int_list[0]
    block_size = 1;
    while block_size <= len(int_list):
        i, j = 0, 0
        while j <= len(int_list):
            j = i + block_size
            sub_list = int_list[i:j]
            _ = calc_sum(sub_list)
            if _ > sum_:
                sum_ = _
            i += 1
        block_size += 1

    return sum_


def calc_sum(int_list):
    sum_= 0
    for i in int_list:
        sum_ += i
    return sum_


def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()

    for line in lines:
        numbers = line.split(",")
        numbers = [int(i) for i in numbers]
        sum_ = largest_sum(numbers)
        print(sum_)


if __name__ == "__main__":
    main()
