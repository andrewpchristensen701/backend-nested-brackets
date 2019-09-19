#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "andrewpchristensen701"

import sys

openp = ['(', '[', '{', '<', '(*']
closep = [')', ']', '}', '>', '*)']


def test_string(entered):
    count = 0
    stack = []
    unbalanced = False
    while entered:
        item = entered[0]

        if entered.startswith("(*"):
            item = "(*"
        elif entered.startswith("*)"):
            item = "*)"
        count += 1

        if item in closep:
            index = closep.index(item)
            matching = open[index]

            if stack.pop() != matching:
                unbalanced = True
                break

        if item in open:
            stack.append(item)

        entered = entered[len(item):]

    if stack or unbalanced:
        return 'NO ' + str(count)
    return 'YES'


def main():
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as o:
            for entered in f:
                read_output = test_string(entered)
                print(read_output)
                o.write(read_output + '\n')


if __name__ == '__main__':
    main()
