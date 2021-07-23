import sys
import time


try:
    with open('poem.txt') as f:
        for line in f:
            if len(line) == 0:
                break
            print(line, end='')
            sys.stdout.flush()
            print('Press ctrl+c now')
            # To make sure it runs for a while
            time.sleep(2)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('!!You canceled the reading from the file.')
