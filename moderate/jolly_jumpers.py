#!/usr/bin/env python2
'''
- CodeEval: Jolly Jumpers
- https://www.codeeval.com/open_challenges/43/
'''

from sys import argv
#import ipdb

def is_jolly(n, numbers):
    #ipdb.set_trace()
    i = 0
    jolly_list = []    
    for i in xrange(n-1):
        difference = (numbers[i] - numbers[i+1]) 
        if difference < 0:
            difference *= -1
        if difference >= n:
            return False
        jolly_list.append(difference)
    
    for i in xrange(1,n):
        if i not in jolly_list:
            return False

    return True

def main():
    with open(argv[1], "rt") as f:
        for line in f:
            numbers =  line.rstrip().split(' ')
            n, numbers = int(numbers[0]), [int (i) for i in numbers[1:]]
            if is_jolly(n, numbers):
                print("Jolly")
            else:
                print("Not jolly")


if __name__ == "__main__":
    main()
