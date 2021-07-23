# coding = utf-8

import pprint

item_list = []
while True:
    print('Please enter the item name and number, like "apple:3", or enter nothing to stop.')
    items = input()
    if items == '':
        break
    item_list += [items]

item_list = [v.split(':') for v in item_list]
sameitem = []
for i in range(len(item_list) - 1):
    j = i + 1
    while j < len(item_list):
        if item_list[i][0] == item_list[j][0]:
            item_list[i][1] = str(int(item_list[i][1]) + int(item_list[j][1]))
            sameitem += [j]
        j += 1
for n in sameitem:
    del item_list[n]

item_dict = dict(item_list)
pprint.pprint(item_dict)
