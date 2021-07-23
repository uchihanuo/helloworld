#! python3
# -*- coding: utf-8 -*-
import os
import time
import pandas as pd

# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")


def find_file(path):
    filename_list = []
    for parent, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.wav'):
                filename_list += file.split()

    pd.DataFrame(
        {'FileName': filename_list,
         'Utterance': [f.split('-')[0] if f.find('-') > 0 else f.split('.')[0] for f in filename_list],
         'Speaker': [f.split('-')[1] if f.find('-') > 0 else '' for f in filename_list],
         'Gender': ['男' if f.find('男') > 0 else '女' if f.find('女') > 0 else '' for f in filename_list]}
    ).to_excel(path + '\\' + os.path.basename(os.path.abspath(path)) + '_' + time.strftime('%Y%m%d%H%M%S') + '.xlsx', index=False)


def main():
    find_file('..')


if __name__ == '__main__':
    main()
