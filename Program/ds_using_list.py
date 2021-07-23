#  It's my shopping list
'''
The past can hurt.
But I think,
you can either run from it or learn from it.
'''
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:',end=' ')
for item in shoplist:
    print(item, end=' ')
#  Add an item
print('\nI also have to buy xbox.')
shoplist.append('xbox')
print('My shopping list is now', shoplist)
#  Sort the list
print('I\'ll sort my shopping list now.')
shoplist.sort()
print('Sorted shopping list is', shoplist)
#  To deal with the list
print('The fist item I will buy is', shoplist[4])
olditem = shoplist[4]
del shoplist[4]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
print(__doc__)
