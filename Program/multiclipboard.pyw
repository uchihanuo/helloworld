#! python3
# coding = utf-8

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# save clipboard content.
if len(sys.argv) is 3 and sys.argv[1].lower() is 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) is 2:
    # list keywords and load content.
    if sys.argv[1].lower() is 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
