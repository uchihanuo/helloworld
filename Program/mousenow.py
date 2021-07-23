#! python3
# -*- coding: utf-8 -*-

import pyautogui, time
from PIL import ImageColor
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
print('Press Ctrl + C to quit.')
print('按 Ctrl + C 退出')
time.sleep(3)
try:
    while True:
        time.sleep(0.07)
        im = pyautogui.screenshot()
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + '  Y: ' + str(y).rjust(4) + '  RBGA: ' + str(im.getpixel((x, y))).rjust(4)
        print(positionStr, end='\n')
        #print('\b' * len(positionStr), flush=True)
except KeyboardInterrupt:
    print('\nDone.')
