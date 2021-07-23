#! python3
# -- coding: utf-8 --

import time
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
# display the program's instructions.
print('Please Enter to begin. afterwards, press enter to "click" the stopwatch. press Ctrl + C to quit.')
input()  # press Enter to begin.
print('Started.')
starttime = time.time()
lasttime = starttime
lapNum = 1
# start tracking the lap times.
try:
    while True:
        input()
        laptime = round(time.time() - lasttime, 2)
        totaltime = round(time.time() - starttime, 2)
        print('Lap #%02d: %s (%s)' % (lapNum, totaltime, laptime), end='')
        lapNum += 1
        lasttime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # handle the Ctrl + C exception to keep its error message from displaying.
    print('\nDone')
