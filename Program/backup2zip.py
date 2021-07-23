#! python3
# -- coding: utf-8 --

import os, zipfile, time


def backuptozip(folder):
    folder = os.path.abspath(folder)
    # number = 1
    # while True:
    zipfilename = os.path.basename(folder) + '_' + time.strftime('%Y%m%d%H%M%S') + '.zip'
    #     if not os.path.exists(zipfilename):
    #         break
    #     number += 1
    # create the zip file.
    print('Create %s...' % (zipfilename))
    backupZip = zipfile.ZipFile(zipfilename, 'w', zipfile.ZIP_DEFLATED)
    # walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # add all the files in this folder to the zip.
        backupZip.write(foldername)
        # add all the files in this folder to the zip.
        for filename in filenames:
            # jump the backup zip files.
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('-----Done-----')


while True:
    zipfolder = str(input('Please enter the folder for zip.'))
    if os.path.exists(zipfolder):
        backuptozip(zipfolder)
        break
    else:
        print('The folder does not exist.')
