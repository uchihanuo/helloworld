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
    filename_list = os.listdir(path)
    pd.DataFrame({
        'FileName': [f for f in filename_list if f.endswith('.dat')],
        'Utterance': [f.split('_')[0] for f in filename_list if f.endswith('.dat')],
        'Date': [f.split('_')[1] for f in filename_list if f.endswith('.dat')],
        'Time': [f.split('_')[2].split('.')[0] for f in filename_list if f.endswith('.dat')]}).to_excel(
        path + '\\' + os.path.basename(os.path.abspath(path)) + '_' + time.strftime('%Y%m%d%H%M%S') + '.xlsx', index=False)


def main():
    find_file('..')


if __name__ == '__main__':
    main()
