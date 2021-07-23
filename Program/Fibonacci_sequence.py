#! python3
# -- coding: utf-8 --

import pprint
import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(filename= 'Fibonacci_sequence_log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Start")

def fit(n):
    logging.debug('Start of fit(%s)' % n)
    return 0 if n is 0 else 1 if n is 1 else fit(n - 1) + fit(n - 2)
    # if n is 0:
    #     return 0
    # elif n is 1:
    #     return 1
    # else:
    #     return fit(n - 1) + fit(n - 2)


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def list_fit(m):
    logging.debug('Start of list_fit(%s)' % m)
    i = 1
    Fibonacci_list = []
    while i <= m:
        logging.debug('i is ' + str(i))
        Fibonacci_list += [fit(i)]
        i += 1
    logging.debug('End of list_fit(%s)' % m)
    return Fibonacci_list


while True:
    Fibon = []
    Num_length = input('Please enter the length of Fibonacci sequence.')
    if Num_length.isdigit():
        print('The Fibonaccie sequence is:')
        # pprint.pprint(list_fit(int(Num_length)))
        for x in fibon(int(Num_length)):
            Fibon += [x]
        pprint.pprint(Fibon)
        break
    else:
        print('Please enter a NUMBER and NOT lower than 0')
logging.debug('End')
