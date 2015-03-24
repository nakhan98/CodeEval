#!/usr/bin/env python2
'''
- CodeEval: Pangrams
- https://www.codeeval.com/open_challenges/37/
'''

from sys import argv

alphabets = "abcdefghijklmnopqrstuvwxyz"

def show_missing_alphas(string1, string2):
    '''return list of chars that are in string1 but not in string2'''
    string2 = string2.lower()
    missing_alphas = [i for i in string1 if i not in string2]
    return missing_alphas


def main():
    with open(argv[1]) as f:
        for line in f:
            missing_alphas = show_missing_alphas(alphabets, line)
            if missing_alphas:
                print( ''.join(missing_alphas) )
            else:
                print("NULL")


if __name__ == "__main__":
    main()
