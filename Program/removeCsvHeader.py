#! python3
# -- coding: utf-8 --

import os, csv
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
# create a folder for CSV files.
os.makedirs('headerRemoved', exist_ok=True)
# loop all files.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        # skip non-CSV file
        continue
    print('Removing header from ' + csvFilename + '...')
    # read the CSV file and skip first row.
    csvRows = []
    csvFileObj = open(csvFilename)
    csvReaderObj = csv.reader(csvFileObj)
    for row in csvReaderObj:
        if csvReaderObj.line_num is 1:
            continue
        csvRows.append(row)
    csvFileObj.close()
    # write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
