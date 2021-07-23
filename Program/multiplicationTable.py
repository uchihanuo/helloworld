#! python3
# -- coding: utf-8 --

import openpyxl
from openpyxl.styles import Font
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")

def calculate(n):
    rows = []
    for i in range(n + 1):
        a_list = [i]
        if i is 0:
            for j in range(1, n + 1):
                a_list += [j]
            rows.append(a_list)
        else:
            for j in range(1, n + 1):
                a_list += [i * j]
            rows.append(a_list)
    wb = openpyxl.Workbook()
    sheet = wb.active
    for row in rows:
        sheet.append(row)
    for r_cell, c_cell in zip(sheet['A'], sheet[1]):
        r_cell.font = openpyxl.styles.Font(bold=True)
        c_cell.font = openpyxl.styles.Font(bold=True)
    sheet['A1'].value = None
    wb.save('Multiplication.xlsx')
    wb.close()
    print('-----Done-----')


while True:
    Num = input('Please enter the target Number.')
    if Num.isdigit():
        calculate(int(Num))
        print("The result in 'Multiplication.xlsx'.")
        break
    else:
        print('Please check your input.')
