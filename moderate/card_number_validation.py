#!/usr/bin/env python2
# CodeEval - Card Number Validation
# https://www.codeeval.com/open_challenges/172/

from sys import argv

def check_number(number_str):
    number_str = number_str[::-1]
    sum_ = 0
    i = 0
    while i < len(number_str):
        if i % 2:
            prod = int(number_str[i]) * 2
            if prod > 9:
                sum_of_digits = 0
                prod_str = str(prod)
                for char in prod_str:
                    sum_of_digits += int(char)
                sum_ += sum_of_digits
            else:
                sum_ += prod
        else:
            sum_ += int( number_str[i] )

        i += 1
    
    if sum_ % 10:
        return 0
    else:
        return 1


def main():
    fh = open(argv[1], "rt")
    for line in fh:
        number_str = line.strip()
        number_str = number_str.replace(" ", "")
        print(check_number(number_str))

    fh.close()


if __name__ == "__main__":
    main()
