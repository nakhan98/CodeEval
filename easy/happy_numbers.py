#!/usr/bin/env python2
# CodeEval - Happy Numbers
# https://www.codeeval.com/open_challenges/39/

import sys
#import ipdb

def sum_of_squares(number):
    '''Return sum of squares of digits'''
    sum = 0
    for i in str(number):
        sum += int(i)**2

    return sum


def is_happy_number(number):
    #ipdb.set_trace()
    list_of_results = [number,]
    
    while True:
        result = sum_of_squares(number)
        if result == 1:
            return 1
        elif result in list_of_results:
            return 0
        else:
            list_of_results.append(result)
            number = result


def main():
    with open(sys.argv[1], 'r') as f:
        file_contents = f.readlines()

    for line in file_contents:
        number = int( line.strip() )
        print( is_happy_number(number) )


if __name__ == "__main__":
    main()
