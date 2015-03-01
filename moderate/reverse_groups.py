#!/usr/bin/env python2
# CodeEval - Reverse Groups
# https://www.codeeval.com/public_sc/71/

from sys import argv

def reverse_group(number_list, k):
    new_list = number_list[:]
    max_ = int(len(new_list)/k) * k 
    i = 0
    j = k
    while j <= max_:
        new_list = new_list[:i] + new_list[i:j][::-1] + new_list[j:]
        i = j 
        j += k
    return new_list


def main():
    f = open(argv[1], "rt")
    for line in f:
        number_list, k = line.strip().split(";")
        k = int(k)
        number_list = number_list.split(",")
        new_list = reverse_group(number_list, k) 
        print( ",".join(new_list) )
    f.close()


if __name__ == "__main__":
    main()
