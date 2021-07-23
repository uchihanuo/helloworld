#! python3
# -- coding: utf-8 --


# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")

import sys, webbrowser, pyperclip


if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open(address)
