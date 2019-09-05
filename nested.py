#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
An app that tests if brackets are valid or not, and then returns an answer in a yes or no form
"""
__author__ = "andrewpchristensen701"

import sys
   
def read_input(filename):
    with open(filename, 'r') as f:
        text= f.read().split("\n")
    return text


def main(args):
    
    bracket_dictionary = {')':'(','}':'{',']':'[','>':'<','*)':'(*'} 
    
    stack = []
    i = 0
    
    closing_brackets = bracket_dictionary.keys()
    opening_brackets = bracket_dictionary.values()
    listed = list(args)
    skip = False
    for index, x in enumerate(listed):
        if skip:
            skip = False
            continue
        else:
            if index != len(listed) - 1:    
                if x == '(' and listed[index + 1] == '*':
                    x = '(*'
                    skip = True
                elif x == '*' and listed[index + 1] == ')':
                    x = '*)'
                    skip = True
            if x in opening_brackets:
                stack.append(x)
                i += 1
            elif x in closing_brackets:  
                i += 1
                if stack[-1] == bracket_dictionary[x]:
                    stack.pop()
                else:
                    return "NO " + str(i)
            else:
                i += 1
    if len(stack) == 0:
        return "YES"
    else:
        i += 1
        return "NO " + str(i)
            
def write_output():
    
    read_output = read_input("input.txt")
    with open("output.txt", "w+") as f:
        for text in read_output:
            f.write(main(text) + "\n") 

if __name__ == '__main__':
    write_output()