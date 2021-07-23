#! python3
# -- coding: utf-8 --

import threading
import time
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')
