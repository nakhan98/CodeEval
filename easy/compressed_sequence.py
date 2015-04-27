#!/usr/bin/env python2
"""
- CodeEval: Compressed Sequence
- https://www.codeeval.com/open_challenges/128/
"""

from sys import argv

def compress_sequence(numbers):
    new_list = []
    length = len(numbers)
    i = 0
    curr = numbers[i]
    count = 1
    while i < length-1:
        if numbers[i+1] == curr:
            count += 1
        else:
            new_list.append( str(count) )
            new_list.append(curr)
            curr = numbers[i+1]            
            count = 1
        i += 1
    new_list.append( str(count) )
    new_list.append(curr)
    return new_list


def main():
    with open(argv[1]) as f:
        for line in f:
            numbers = line.rstrip().split(' ')
            compressed_sequence = compress_sequence(numbers)
            print( ' '.join(compressed_sequence) )


if __name__ == "__main__":
    main()
