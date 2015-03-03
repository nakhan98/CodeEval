#!/usr/bin/env python2
# CodeEval - Counting Primes
# https://www.codeeval.com/open_challenges/63/

from sys import argv

def is_prime(number):
    ''' Return True if number is a prime, else False'''
    if number < 2: 
        return False

    # Only need to check up to square root
    limit = int(number**0.5 + 1)

    for i in range(2, limit):
        if number%i == 0:
            return False
    return True


def main():
    with open(argv[1], "rt") as f:
        for line in f:
            _ = line.strip().split(",")
            integers = [int(i) for i in _]
            integers = range(integers[0], integers[1]+1)
            count = 0
            for integer in integers:
                if is_prime(integer):
                    count += 1
            print(count)


if __name__ == "__main__":
    main()
