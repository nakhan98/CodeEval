#!/usr/bin/env python2
# CodeEval - Decimel to Binary
# https://www.codeeval.com/browse/27/
# Using my own algos here instead of python built-ins

from sys import argv

def power(x,y):
    '''Raise x to power y'''
    orig_y = y
    if y < 0:
        y *= -1
    i = 0
    a = 1
    while i < y:
        a = a * x
        i += 1

    if orig_y < 0:
        return 1.0/a
    else:
        return a
    

def convert_to_binary(dn):
    ''' Convert decimel integer to binary string'''
    if dn == 0:
        return dn
    powers_collected = []
    exponent = 0
    while True:
        if power(2, exponent) == dn:
            dn = 0
            powers_collected.append(exponent)
            break
        elif power(2, exponent) > dn:
            exponent -= 1
            dn -= power(2,exponent)
            powers_collected.append(exponent)
            exponent = 0
        else:
            exponent += 1

    binary_number_list = [0] * (powers_collected[0]+1)
    for i in powers_collected:
        index = powers_collected[0] - i
        binary_number_list[index] = 1
    
    _ = [str(i)  for i in binary_number_list]
    binary_number_str = "".join(_)
    return binary_number_str


def main():
    fh = open(argv[1], "rt")
    for line in fh:
        number = int(line)
        binary_rep = convert_to_binary(number)
        print(binary_rep)

    fh.close()


if __name__ == "__main__":
    main()
