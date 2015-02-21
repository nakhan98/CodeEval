#!/usr/bin/env python2
# Codeeval - Prime Palindrome
# https://www.codeeval.com/open_challenges/3/

list_of_prime_palindromes = []

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


def is_palindrome(number):
    '''Return True if number is a palindrome'''
    number_string = str(number)
    if number_string == number_string[::-1]: 
        return True
    else:
        return False


def main():
    for number in range(1,1000):
        if is_prime(number) and is_palindrome(number):
            list_of_prime_palindromes.append(number)
    
    print(list_of_prime_palindromes[-1])
    

if __name__ == "__main__":
    main()
