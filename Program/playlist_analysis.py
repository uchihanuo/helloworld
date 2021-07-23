#! python3
# -*- coding: utf-8 -*-

import plistlib
import numpy as np
from matplotlib import pyplot as plt
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")

def findDuplicates(filename):
    print('Finding duplicate tracks in %s...' % filename)
    # read in a playlist
    plist = plistlib.load(filename)
    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # create a track name dictionary
    trackNames = {}
    # iterate through the tracks
    for trackID, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # look for existing entries
            if name in trackNames:
                # if a name and duration match, increment the count
                # round the track length to the nearest sound
                if duration // 1000 == trackNames[name][0] // 1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count + 1)
            else:
                # add dictionary entry as tuple (duration, count)
            trackNames[name] = (duration, 1)
        except:
            # ignore
            pass
