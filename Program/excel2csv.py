#! python3
# -- coding: utf-8 --

import os, openpyxl, csv
from os.path import splitext
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
# create a folder for CSV files.
os.makedirs('csvfile', exist_ok=True)
# loop all files.
for excelFile in os.listdir(os.getcwd()):
    if not excelFile.endswith(('.xlsx', '.xls')):
        continue  # skipping non-excel file.
    print('Converting file from ' + excelFile + '...')
    # copy excel file content.
    excelfileObj = openpyxl.load_workbook(excelFile)
    for sheet in excelfileObj.sheetnames:
        excelRows = []
        for i in range(1, excelfileObj[sheet].max_row + 1):
            a_list = []
            for row in excelfileObj[sheet][i]:
                a_list.append(row.value)
            excelRows.append(a_list)
            # create csv file.
            with open(os.path.join('csvfile', splitext(excelFile)[0] + '_' + sheet + '.csv'), 'w', newline='') as csvFile:
                csvWriter = csv.writer(csvFile)
                for row in excelRows:
                    csvWriter.writerow(row)
    excelfileObj.close()
    print(splitext(excelFile)[0] + '_' + sheet + '.csv converted done.')
print('-----Done-----')
