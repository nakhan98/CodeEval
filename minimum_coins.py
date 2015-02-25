#!/usr/bin/env python2
# CodeEval - Minimum Coins
# https://www.codeeval.com/open_challenges/74/

from sys import argv

coins = (5, 3, 1)

def calc_numb_coins(amount):
    coins_to_return = []
    for i in coins:
        quotient = amount / float(i)
        if quotient > 1:
            number_of_coins = int(quotient)
            [coins_to_return.append(i) for _ in range(number_of_coins)]
            amount -= number_of_coins * i
        elif quotient == 1:
            coins_to_return.append(i)
            amount -= i 
        if not amount:
            return coins_to_return
    

def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()

    for line in lines:
        amount = int(line)
        numb_coins = calc_numb_coins(amount)
        print(len(numb_coins))


if __name__ == "__main__":
    main()
