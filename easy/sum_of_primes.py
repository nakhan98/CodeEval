#!/usr/bin/env python 2
# CodeEval - Sum of Primes
# https://www.codeeval.com/open_challenges/4/

list_of_primes = []

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


def main():
    sum = 0
    number = 1

    while len(list_of_primes) < 1000:
        if is_prime(number):
            list_of_primes.append(number)
        number += 1 
    
    for prime in list_of_primes:
        sum += prime
    
    print(sum)


if __name__ == "__main__":
    main()
