# coding = utf-8

import re


def len_num_case(a_str):
    if len(a_str) <= 8:
        return False
    if re.compile(r'[A-Z]').search(a_str).group() is None:
        return False
    if re.compile(r'[a-z]').search(a_str).group() is None:
        return False
    if re.compile(r'[0-9]').search(a_str).group() is None:
        return False
    else:
        return True


while True:
    passwords_str = str(input('Please enter your pass words.'))
    if len_num_case(passwords_str):
        print('The passwords is strange.')
        break
    else:
        print('The passwords is NOT enough strange.')
