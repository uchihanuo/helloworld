#! python3
# -- coding: utf-8 --


# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
print('\n'.join([''.join([('LoveYueyue'[(x-y) % 10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ')for x in range(-30, 30)])for y in range(15, -15, -1)]))

print('\n'.join([' '.join(['%-2s*%2s = %-4s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))
