#!/usr/bin/env python2
# CodeEval - Prime Numbers
# https://www.codeeval.com/open_challenges/46

import sys

def is_prime(number):
    ''' Return True if number is a prime, else False'''
    if number < 2: 
        return False

    # Only need to check up to half
    limit = number/2 + 1

    for i in range(2, limit):
        if number%i == 0:
            return False
    return True


def find_primes(integer):
    list_of_ints = []
    for i in range(2, integer):
        if is_prime(i):
            list_of_ints.append(i)
    
    return list_of_ints


def main():
    with open(sys.argv[1], "rt") as f:
        lines = f.readlines()

    for line in lines:
        integer = int(line)
        primes = find_primes(integer)
        primes = [str(i) for i in primes]
        print( ",".join(primes))


if __name__ == "__main__":
    main()
