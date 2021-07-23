import readline
import rlcompleter
import atexit
import os
# tab autocomplete
readline.parse_and_bind('tab: complete')
# history file
histfile = os.path.join(os.environ['Home', '.pythonhistory'])
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.worte_history_file, histfile)
del os, histfile, readline, rlcompleter
