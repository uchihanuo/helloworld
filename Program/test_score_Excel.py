#! python3
# -- coding: utf-8 --

import openpyxl, pprint
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
print('Opening Workbook.....')
wb = openpyxl.load_workbook('test_score.xlsx')
sheet = wb.active
courseDate = {}
print('Reading rows.....')
for row in range(2, sheet.max_row + 1):
    courseNum = sheet['B' + str(row)].value
    # ID = sheet['A' + str(row)].value
    score = 0 if sheet['C' + str(row)].value is None else sheet['C' + str(row)].value
    # make sure for this courseDate is exists
    courseDate.setdefault(courseNum, {'TotalNum': 0, 'AVG': 0})
    courseDate[courseNum]['TotalNum'] += 1
    courseDate[courseNum]['AVG'] += int(score)
for scores in courseDate.values():
    scores['AVG'] = float('%.02f' % (scores['AVG'] / scores['TotalNum']))
print('Writing results.....')
resultFile = open('test_score_result.py', 'w')
resultFile.write('allDate = ' + pprint.pformat(courseDate))
resultFile.close()
print('-----Done-----')
