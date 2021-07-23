#! python3
# -- coding: utf-8 --


def howmany_list(a_list):
    if a_list[1:]:
        return 1 + howmany_list(a_list[1:])
    else:
        return 1

input('Enter number.')
