#!/usr/bin/env python2
# CodeEval - Cash Register
# https://www.codeeval.com/open_challenges/54/

from sys import argv

cash_register = {
    'PENNY': .01,
    'NICKEL': .05,
    'DIME': .10,
    'QUARTER': .25,
    'HALF DOLLAR': .50,
    'ONE': 1.00,
    'TWO': 2.00,
    'FIVE': 5.00,
    'TEN': 10.00,
    'TWENTY': 20.00,
    'FIFTY': 50.00,
    'ONE HUNDRED': 100.00
}


def cc(float_):
    '''Convert to cents'''
    return int(float_*100)


def calc_change(PP, CH):
    change = cc(CH) - cc(PP)

    bills_coins = sorted(cash_register.iterkeys(), 
            key=lambda k: cash_register[k])[::-1] # sort keys according to their values

    for bill_coin in bills_coins:
        if change == cc(cash_register[bill_coin]):
            return (bill_coin,)

    i = 0
    change_bills_coins = []
    while change:
        bill_coin = bills_coins[i]
        _ = float(change) / cc(cash_register[bill_coin])
        if _ > 1:
            amount = int(_)
            change_bills_coins += [bill_coin]*amount
            change = change - amount * cc(cash_register[bill_coin])
        elif _ == 1:
            change_bills_coins.append(bill_coin)
            return change_bills_coins
            
        i += 1
    return change_bills_coins


def main():
    with open(argv[1], "rt") as f:
        lines = f.readlines()
    
    for line in lines:
        PP, CH = [float(i) for i in line.strip().split(";")]
        if CH < PP:
            print("ERROR")
        elif CH == PP:
            print("ZERO")
        else:
            change = calc_change(PP, CH)
            print(",".join(change))


if __name__ == "__main__":
    main()
