#!/usr/bin/env python2
# Codeeval - FizzBuzz

import sys

def fizzbuzz(numbers):
        x, y, z = numbers
        for i in range(1, z+1):
            if i%x == 0 and i%y == 0:
                sys.stdout.write("FB ")
            elif i%x == 0:
                sys.stdout.write("F ")
            elif i%y ==0:
                sys.stdout.write("B ")
            else:
                sys.stdout.write("%d " % i)
            
        sys.stdout.write("\n") 


def main():
    if len(sys.argv) != 2:
        sys.exit("Error... usage is 'python2 fizzbuzz.py2 [file]")

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    for line in lines:
        numbers = [int(i) for i in line.split()] # create a list of ints
        fizzbuzz(numbers)


if __name__ == "__main__":
    main()
