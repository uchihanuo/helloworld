#! python3
# -- coding: utf-8 --

import time, subprocess
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")


def countdown(n):
    timeleft = n
    while timeleft > 0:
        print(timeleft, end='\n')
        time.sleep(1)
        timeleft -= 1
    subprocess.Popen(['start', 'alarm.wav'], shell=True)
