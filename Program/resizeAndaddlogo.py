#! python3
# -- coding: utf-8 --

import os
from PIL import Image
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
square_fit_size = 300
logo_filename = 'catlogo.png'
logoim = Image.open(logo_filename)
os.makedirs('withlogo', exist_ok=True)

for filename in os.listdir('.'):
    if filename == logo_filename or not filename.endswith(('.png', '.jpg')):
        continue
    im = Image.open(filename)
    im_w, im_h = im.size
    # check if image needs to be resize.
    if im_w > square_fit_size or im_h > square_fit_size:
        print('Resize %s...' % (filename))
        if im_w > im_h:
            im_h = int((square_fit_size / im_w) * im_h)
            im_w = square_fit_size
        else:
            im_w = int((square_fit_size / im_h) * im_w)
            im_h = square_fit_size
        im = im.resize((im_w, im_h))
    # add the logo.
    print('Adding logo to %s...' % (filename))
    logocopy = logoim.copy()
    logocopy_w, logocopy_h = logocopy.size
    logocopy_h = int((im_w / 4 /logocopy_w) * logocopy_h)
    logocopy_w = int(im_w / 4)
    logocopy = logocopy.resize((logocopy_w, logocopy_h))
    im.paste(logocopy, (im_w - logocopy_w, im_h - logocopy_h), logocopy)
    im.save(os.path.join('withlogo', filename))
    print('-----Done-----')
