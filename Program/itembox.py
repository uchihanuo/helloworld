# coding = utf-8


def displayInventory(Inventory): # for calculating total number and print the items list
    Itemnum = 0
    print('Inventory'.center(19))
    for k, v in Inventory.items():
        print(k.ljust(13, '-') + str(v).rjust(6))
        Itemnum += int(v)
    print('Total'.ljust(13, '.') + str(Itemnum).rjust(6))


def enterInventory(item): # for converting the 'list' to 'dict' and combining the same item
    item_list = [v.split(':') for v in item]
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
    return item_dict


Inventory_bag = []
while True:
    print('Please enter your items and numbers, like this "apple:3", or enter nothing to end.')
    items = input()
    if items == '':
        break
    Inventory_bag += [items]

Inventory_dict = enterInventory(Inventory_bag)
displayInventory(Inventory_dict)
