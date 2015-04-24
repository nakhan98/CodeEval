#!/usr/bin/env python2
'''
- CodeEval: Flavius Josephus
- https://www.codeeval.com/open_challenges/75/
'''

from sys import argv

def get_order_executions(n, m):
    execution_order = []
    people = range(n)
    init = - 1
    while people:
        exec_index = init + m
        if exec_index >= len(people):
            exec_index = exec_index % len(people)
        removed = people.pop(exec_index)
        execution_order.append(removed)
        init = exec_index - 1
    return execution_order


def main():
    with open(argv[1], "rt") as f:
        for line in f:
            n, m = (int(i) for i in line.strip().split(','))
            execution_order = get_order_executions(n, m)
            print(' '.join( [str(i) for i in execution_order] ))


if __name__ == "__main__":
    main()
