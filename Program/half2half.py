#! python3
# -- coding: utf-8 --


import logging, random
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Start of program.")

guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('guess is %s' % guess)
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('toss is %s' % toss)
map = {'tails': 0, 'heads': 1}
if map[guess] == toss:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if map[guesss] == toss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('End of program.')
