#! python3
# -*- coding: utf-8 -*-

import pandas as pd
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")

a_dict = []
item_box = {}
while True:
    item = input('Please enter the item\'s name.')
    num = input('Please enter the item\'s number.')
    if item == '' or num == '':
        break
    a_dict += [{item: int(num)}]
data_df = pd.DataFrame(a_dict)
for name in data_df.columns.tolist():
    item_box.update({name: data_df[name].sum()})
print(pd.Series(item_box))
