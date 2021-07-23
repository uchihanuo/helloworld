# coding = utf-8

import re


def strip_sub(a_str, c = None):
    if c is None:
        strip_mo = re.compile(r'\s*(.*)\s*')
        print(strip_mo.sub(r'\1', a_str))
    else:
        strip_mo = re.compile(c)
        print(strip_mo.sub(r'', a_str))


print('This is a function like Strip().')

Your_str = str(input('Please enter your strings:'))
Your_case = input('Please enter your case:')
strip_sub(Your_str, Your_case)
