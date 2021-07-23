#! python3
# -*- coding: utf-8 -*-


# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")


def test_list_pre():
    prepare_list = locals()
    for i in range(16):
        prepare_list['list_' + str(i)] = []
        prepare_list['list_' + str(i)].append('I\'m the ' + str(i) + 'th list.')
    for i in prepare_list:
        print(i, prepare_list[i])


if __name__ == '__main__':
    test_list_pre()
