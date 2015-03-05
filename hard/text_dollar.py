#!/usr/bin/env python2
# CodeEval - Text Dollar
# https://www.codeeval.com/open_challenges/52/

from sys import argv

single_digits = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
teens = ("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
double_digits = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")


def convert_number(number_str):
    '''Convert 3 digit numbers to English equivelant'''
    number_str = number_str.zfill(3)
    number = []
    if number_str[0] != "0":
        hundreds = int(number_str[0])
        string = single_digits[hundreds] + "Hundred" 
        number.append(string)
    
    if number_str[1] == "0":
        string = single_digits[ int(number_str[2]) ]
        number.append(string)
    elif number_str[1] == "1":
        string = teens[ int(number_str[2]) ]
        number.append(string)
    else:
        number.append( double_digits[ int(number_str[1]) ] )
        number.append( single_digits[ int(number_str[2]) ] )

    return "".join(number)


def text_number(number_str):
    number_str = number_str.zfill(9)
    number = []
    if int(number_str[:3]):
        millions = str( int(number_str[:3]) )
        millions = convert_number(millions) + "Million"
        number.append(millions)

    if int(number_str[3:6]):
        thousands = str( int(number_str[3:6]) )        
        thousands = convert_number(thousands) + "Thousand"
        number.append(thousands)

    if int(number_str[6:]):
        hundreds = str( int(number_str[6:]) )
        hundreds = convert_number(hundreds)
        number.append(hundreds)

    return "".join(number)


def main():
    f = open(argv[1], "rt")
    for line in f:
        numbers_str = line.strip()
        dollars = text_number(numbers_str)
        print(dollars+"Dollars")
    f.close() 


if __name__ == "__main__":
    main()
