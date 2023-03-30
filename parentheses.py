#https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python

#removes all parentheses and contents therein, including nested parens

import re

def remove_parentheses(s):
    while re.search(r'\([^()]*\)', s):
        s = re.sub(r'\([^()]*\)', '', s)
    return s
