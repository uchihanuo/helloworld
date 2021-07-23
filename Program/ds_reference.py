print('Simple assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana', 'xbox']
mylist = shoplist

del shoplist[0]
print('Shoplist are', shoplist)
print('Mylist are', mylist)

mylist = shoplist[:]

del shoplist[0]
print('Shoplist are', shoplist)
print('Mylist are', mylist)
