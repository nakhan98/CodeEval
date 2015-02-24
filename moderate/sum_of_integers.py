#!/usr/bin/env python2
# CodeEval - Sum of Integers 
# https://www.codeeval.com/open_challenges/17/

from sys import argv

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


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
        #sum_ = largest_sum(numbers)
        sum_ = max_subarray(numbers)
        print(sum_)


if __name__ == "__main__":
    main()
